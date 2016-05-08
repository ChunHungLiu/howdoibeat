#!/usr/bin/python
# This class handles the analysis of the data fetched from the Riot Games API.
# Author: alvin.lin.dev@gmail.com (Alvin Lin)

from riot_api import RiotApi
from util import Util

import json

class DataAnalyzer():

    def __init__(self, static_data):
        self.static_data = static_data

    @staticmethod
    def create():
        champions = RiotApi.get_champions()
        return DataAnalyzer({
            "champions": champions
        })

    def get_summoner_mastery_info(self, summoner_name):
        data = {}
        summoner_id = RiotApi.get_summoner_id(summoner_name)
        if not summoner_id:
            return None
        mastery = RiotApi.get_champion_mastery_data(summoner_id)
        main_role = {}
        for champion in mastery:
            champion_info = self.static_data["champions"][str(
                champion["championId"])]
            for tag in champion_info["tags"]:
                if tag in main_role:
                    main_role[tag] += champion["championPoints"]
                else:
                    main_role[tag] = champion["championPoints"]
        data["mastery"] = mastery
        data["main_role"] = sorted(main_role, key=main_role.get)[::-1]
        return data

if __name__ == "__main__":
    d = DataAnalyzer.create()
    print d.get_summoner_mastery_info("omgimanerd")
