"""
  @Filename:    ibm_mq_client.py
  @Author:      Rasika Ranawaka
  @Date:        22/01/2024
"""
import allure
import pymqi

from configuration_settings import ConfigurationSettings


class MQClient:

    def __init__(self):
        config: dict = ConfigurationSettings.get_config()
        self.queue_manager = config["queue_manager"]
        self.channel = config["channel"]
        self.host = config["host"]
        self.port = config["port"]
        self.conn_info = '%s(%s)' % (self.host, self.port)

    def send_message(self, queue_name: str, message: str) -> None:
        with allure.step(f"Sending below message to queue: {queue_name}' of queue manager: {self.queue_manager} \n {message}"):
            q_manager: pymqi.QueueManager = pymqi.connect(self.queue_manager, self.channel, self.conn_info)
            queue = pymqi.Queue(q_manager, queue_name)
            queue.put(message)
            queue.close()
            q_manager.disconnect()

