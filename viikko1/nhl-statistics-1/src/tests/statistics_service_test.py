import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),   # =16
            Player("Lemieux", "PIT", 45, 54), # =99
            Player("Kurri",   "EDM", 37, 53), # =90
            Player("Yzerman", "DET", 42, 56), # =98
            Player("Gretzky", "EDM", 35, 89)  # =124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_search_not_found_returns_none(self):
        player = self.stats.search("Nobody")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")
        names = [p.name for p in team_players]
        self.assertCountEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_returns_empty_list_for_unknown_team(self):
        team_players = self.stats.team("XYZ")
        self.assertEqual(team_players, [])

    def test_top_by_points(self):
        top3 = self.stats.top(3, SortBy.POINTS)
        names = [p.name for p in top3]
        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_by_goals(self):
        top2 = self.stats.top(2, SortBy.GOALS)
        names = [p.name for p in top2]
        self.assertEqual(names, ["Lemieux", "Yzerman"])

    def test_top_by_assists(self):
        top2 = self.stats.top(2, SortBy.ASSISTS)
        names = [p.name for p in top2]
        self.assertEqual(names, ["Gretzky", "Yzerman"])

    def test_top_how_many_more_than_available_returns_all(self):
        top10 = self.stats.top(10, SortBy.POINTS)
        self.assertEqual(len(top10), 5)

    def test_top_with_non_positive_how_many_returns_empty(self):
        self.assertEqual(self.stats.top(0), [])
        self.assertEqual(self.stats.top(-1), [])

if __name__ == '__main__':
    unittest.main()
