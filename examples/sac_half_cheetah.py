'''
An example launcher of running SAC with pendulum.

Noted that this has not been benchmarked yet.
TODO: Add benchmarking results here.
'''
from gym.envs.mujoco import HalfCheetahEnv
from garage.experiment import run_experiment
from garage.envs import GarageEnv

from meta_agents.algos.sac import SAC
from meta_agents.policies import GaussianMLPPolicy
from meta_agents.experiment import LocalRunner
from meta_agents.q_functions import ContinuousMLPQFunction
from meta_agents.replay_buffer import SimpleReplayBuffer


def run_exp(*_):
    with LocalRunner() as runner:
        env = GarageEnv(HalfCheetahEnv())
        # q-functions
        qf1 = ContinuousMLPQFunction(env_spec=env.spec)
        qf2 = ContinuousMLPQFunction(env_spec=env.spec)
        # replay buffer
        replay_buffer = SimpleReplayBuffer(
            env_spec=env.spec,
            size_in_transitions=int(1e6),
            time_horizon=100,)
        # policy
        policy = GaussianMLPPolicy(env_spec=env.spec)
        # algorithm
        algo = SAC(
            env_spec=env.spec,
            policy=policy,
            qfs=[qf1, qf2],
            replay_buffer=replay_buffer,)
        # setup and train
        runner.setup(algo, env)
        runner.train(n_epochs=100, batch_size=400)


run_experiment(
    run_exp,
    exp_prefix='sac_halfcheetah',
    snapshot_mode='last',
)
