#!/usr/bin/env python2
# -*-coding:UTF-8 -*

from pubsublogger import publisher

import Helper


if __name__ == "__main__":
    publisher.channel = "Queuing"

    config_section = 'PubSub_Categ'
    config_channel = 'channel_0'
    subscriber_name = 'creditcard_categ'

    h = Helper.Redis_Queues(config_section, config_channel, subscriber_name)
    h.zmq_sub(config_section)
    h.redis_queue_subscribe(publisher)
