
from garage.envs import GarageEnv
from garage.experiment import run_experiment
from gym.envs.mujoco import HalfCheetahEnv

from meta_agents.algos.trpo import TRPO
from meta_agents.baselines import LinearFeatureBaseline
from meta_agents.experiment import LocalRunner
from meta_agents.policies import GaussianMLPPolicy


def run_exp(snapshot_config, *_):
    with LocalRunner(snapshot_config) as runner:
        env = GarageEnv(HalfCheetahEnv())

        baseline = LinearFeatureBaseline()
        policy = GaussianMLPPolicy(env_spec=env.spec)

        algo = TRPO(policy=policy, baseline=baseline)

        runner.setup(algo=algo, env=env)
        runner.train(n_epochs=100, batch_size=512)


run_experiment(
    run_exp,
    exp_prefix='trpo_halfcheetah',
    snapshot_mode='last',
)