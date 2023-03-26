from channels.generic.websocket import WebsocketConsumer
from random import randint
from time import sleep
import json
import numpy as np
from nav import Nav

GRAVITY = 9.80665  # m / s


class MechanizationConsumer(WebsocketConsumer):
    nav = None

    def connect(self):
        self.accept()

        for i in range(1000):
            self.send(json.dumps({'message': randint(1, 100)}))
            sleep(1)

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # start, update, or end nav here based on `message`

        self.send(text_data=json.dumps({"message": message}))

    def set_nav(self, displacement=None, is_supercharged=None, drag_coeff=None):
        self.nav = Nav(
            smoothing_critical_freq=0.03,
            vz_depth=3,
            period=0.01,
            algo='madgwick',
            smooth_fc=True,
            fc_smoothing_critical_freq=0.02,
            imu_damping=0.05,
            fc_reduction_factor=0.5,
            displacement=displacement,
            is_supercharged=is_supercharged,
            drag_coeff=drag_coeff,
        )

    def set_params(self, displacement, is_supercharged, drag_coeff=None):
        if self.nav is None:
            print('WARNING: Navigation not initialized. Call set_nav to initialize.')
            return
        self.nav.set_vehicle_params(displacement, is_supercharged, drag_coeff)

    def run_nav(self, batch):
        if self.nav is None:
            print('WARNING: Navigation not initialized. Call set_nav to initialize.')
            return

        for data in batch:
            t, ax, ay, az, ax_nog, ay_nog, az_nog, gx, gy, gz, mx, my, mz, lat, long, alt, heading, speed = data

            acc = np.array([ax * GRAVITY, ay * GRAVITY, az * GRAVITY])
            acc_nog = np.array([ax_nog * GRAVITY, ay_nog * GRAVITY, az_nog * GRAVITY])
            gyr = np.array([gx, gy, gz])
            mag = np.array([mx, my, mz])

            self.nav.process_imu_update(t, acc, acc_nog, gyr, mag)
            if lat is not None:
                self.nav.process_gps_update(t, lat, long, alt, heading, speed)

        return self.nav.get_fuel()

    def end_nav(self):
        trip_metrics = self.nav.get_trip_metrics()
        self.nav = None
        return trip_metrics
