from model.core.Environment import Environment
from model.core.Agent import Agent

def test_put_agent():
    env = Environment(10, 10, False)
    agent = Agent(env, 0, 0, 0, 0, None)
    env.put_agent(agent)
    assert agent in env.agents

def test_put_agent_on_another():
    env = Environment(10, 10, False)
    agent1 = Agent(env, 0, 0, 0, 0, None)
    agent2 = Agent(env, 0, 0, 0, 0, None)
    env.put_agent(agent1)
    assert agent1 in env.agents
    env.put_agent(agent2)
    assert agent1 in env.agents
    assert agent2 not in env.agents

def test_remove_agent():
    env = Environment(10, 10, False)
    agent = Agent(env, 0, 0, 0, 0, None)
    env.put_agent(agent)
    assert agent in env.agents
    env.remove_agent(agent)
    assert agent not in env.agents
