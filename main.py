import dotenv
dotenv.load_dotenv()

from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew
from tools import count_letters

@CrewBase
class TranslatorCrew:
    
    @agent
    def translator_agent(self):
        return Agent(
            config =self.agents_config["translator_agent"]
        )

    @agent
    def counter_agent(self):
        return Agent(
            config = self.agents_config["translator_agent"]
        )
    
    @task
    def translate_task(self):
        """from english to italian"""
        return Task(
            config = self.tasks_config["translate_task"]
        )

    @task
    def retranslate_task(self):
        """from italian to french"""
        return Task(
            config = self.tasks_config["retranslate_task"]
        )

    @task
    def count_task(self):
        """from italian to french"""
        return Task(
            config = self.tasks_config["count_task"],
            tools=[count_letters]

        )

    @crew
    def assemble_crew(self):
        return Crew(
            agents = self.agents, #우리가 따로 저장하지 않았지만 decorator들이 알아서 추가해줌
            tasks = self.tasks,
            verbose = True #see the log on console
        )

TranslatorCrew().assemble_crew().kickoff(inputs={"sentence":"I'm Boyoon and I'm from South Korea. I work as a data scientist and a python tutor."})