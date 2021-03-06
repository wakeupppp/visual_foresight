import numpy as np
import os
from visual_mpc.agent.benchmarking_agent import BenchmarkAgent
from visual_mpc.envs.robot_envs.autograsp_env import AutograspEnv
from visual_mpc.policy.cem_controllers.pixel_cost_controller import PixelCostController
from visual_mpc.envs.robot_envs.util.topic_utils import IMTopic
from visual_mpc.policy.cem_controllers.samplers import CorrelatedNoiseSampler


BASE_DIR = '/'.join(str.split(__file__, '/')[:-1])


env_params = {
    'camera_topics': [IMTopic('/front/image_raw')],
    'robot_type': 'baxter',
    'gripper_attached': 'baxter_gripper',
    'cleanup_rate': -1,
    'duration': 3.5,
    'save_video': True
}

agent = {'type' : BenchmarkAgent,
         'env': (AutograspEnv, env_params),
         'data_save_dir': BASE_DIR,
         'T': 15,  #number of commands per episodes (issued at control_rate / substeps HZ)
         'image_height': 48,
         'image_width': 64,
         'make_final_recording': ''
}

policy = {
    'type': PixelCostController,
    'verbose_every_iter': True,
    'replan_interval': 13,
    'num_samples': 600,
    'start_planning': 2,
    'selection_frac': 2./3,
    'predictor_propagation': True,   # use the model get the designated pixel for the next step!
    'nactions': 13,

    "model_params_path": "~/models/baxter_only/experiment_state-2019-07-06_22-22-55.json",
    "model_restore_path": "~/models/baxter_only/household/checkpoint_70000/model-70000",
    # "model_restore_path": "~/models/baxter_only/baxter_cloth/checkpoint_60000/model-60000",

    "sampler": CorrelatedNoiseSampler

}

config = {
    'experiment_name': 'household',
    'traj_per_file':128,
    'save_data': True,
    'save_raw_images' : True,
    'start_index':0,
    'end_index': 30000,
    'agent': agent,
    'policy': policy,
    'ngroup': 1000,
    'nshuffle' : 200
}
