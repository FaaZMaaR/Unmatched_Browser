import sqlite3

class UnmatchedData:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.curs = self.db.cursor()
        
    def fetchSetData(self):
        request = "SELECT * FROM \"set\";"
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchSetHeroesData(self, id):
        request = f"SELECT \"hero\".\"id\", \"hero\".\"s_name\", \"hero\".\"name\", \"hero\".\"hp\", \"hero\".\"move\", \"attack_type\".\"name\" FROM \"hero\" LEFT JOIN \"set\" ON \"hero\".\"set_id\" = \"set\".\"id\" LEFT JOIN \"attack_type\" ON \"hero\".\"attack_type_id\" = \"attack_type\".\"id\" WHERE \"set\".\"id\" = {id};"
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchSetMapsData(self, id):
        request = f"SELECT \"map\".\"id\", \"map\".\"s_name\", \"map\".\"name\", \"map\".\"start_spaces\", \"map\".\"zone_count\", \"map\".\"space_count\" FROM \"map\" LEFT JOIN \"set\" ON \"map\".\"set_id\" = \"set\".\"id\" WHERE \"set\".\"id\" = {id};"
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchHeroData(self):
        request = "SELECT \"hero\".\"id\", \"hero\".\"name\", \"hero\".\"hp\", \"hero\".\"move\", \"hero\".\"count\", \"hero\".\"ability\", \"hero\".\"s_name\", \"attack_type\".\"name\", \"set\".\"name\" FROM \"hero\" LEFT JOIN \"set\" ON \"hero\".\"set_id\" = \"set\".\"id\" LEFT JOIN \"attack_type\" ON \"hero\".\"attack_type_id\" = \"attack_type\".\"id\";"
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchHeroSidekickData(self, heroId):
        request = f"SELECT \"sidekick\".\"name\", \"sidekick\".\"hp\", \"sidekick\".\"count\", \"sidekick\".\"s_name\", \"attack_type\".\"name\" FROM \"sidekick\" LEFT JOIN \"attack_type\" ON \"sidekick\".\"attack_type_id\" = \"attack_type\".\"id\" WHERE \"sidekick\".\"id\" = {heroId};"
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchHeroCardsData(self, heroId):
        request = f"SELECT \"card\".\"id\", \"card\".\"name\", \"card\".\"count\" FROM \"card\" LEFT JOIN \"hero\" ON \"card\".\"hero_id\" = \"hero\".\"id\" WHERE \"hero\".\"id\" = {heroId} ORDER BY \"card\".\"number\";"
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchMapData(self):
        request = f"SELECT \"map\".\"id\", \"map\".\"name\", \"map\".\"start_spaces\", \"map\".\"zone_count\", \"map\".\"space_count\", \"map\".\"s_name\", \"set\".\"name\" FROM \"map\" LEFT JOIN \"set\" ON \"map\".\"set_id\" = \"set\".\"id\";"
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchCardData(self):
        request = f"SELECT \"card\".\"id\", \"card\".\"name\", \"card_type\".\"name\", \"card\".\"value\", \"card\".\"boost\", \"hero\".\"name\", \"card\".\"count\" FROM \"card\" LEFT JOIN \"card_type\" ON \"card\".\"type_id\" = \"card_type\".\"id\" LEFT JOIN \"hero\" ON \"card\".\"hero_id\" = \"hero\".\"id\" ORDER BY \"card\".\"name\";"
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchCardInfoData(self, cardId):
        request = f"SELECT \"card\".\"name\", \"card_type\".\"name\", \"card\".\"value\", \"card\".\"banner\", \"card\".\"boost\", \"card\".\"main_effect\", \"card\".\"immediately\", \"card\".\"during_combat\", \"card\".\"after_combat\", \"hero\".\"name\", \"card\".\"count\", \"hero\".\"s_name\", \"card\".\"number\" FROM \"card\" LEFT JOIN \"card_type\" ON \"card\".\"type_id\" = \"card_type\".\"id\" LEFT JOIN \"hero\" ON \"card\".\"hero_id\" = \"hero\".\"id\" WHERE \"card\".\"id\" = {cardId};"
        self.curs.execute(request)
        return self.curs.fetchall()[0]