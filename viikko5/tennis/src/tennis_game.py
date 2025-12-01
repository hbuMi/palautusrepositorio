class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_words = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1

    def _score_name(self, points):
        return self.score_words.get(points)

    def get_score(self):
        if self.player1_score == self.player2_score:
            if self.player1_score in (0, 1, 2):
                return f"{self.score_words[self.player1_score]}-All"
            else:
                return "Deuce"

        if self.player1_score >= 4 or self.player2_score >= 4:
            diff = self.player1_score - self.player2_score
            if diff == 1:
                return f"Advantage {self.player1_name}"
            if diff == -1:
                return f"Advantage {self.player2_name}"
            if diff >= 2:
                return f"Win for {self.player1_name}"
            else:
                return f"Win for {self.player2_name}"

        player1_score_word = self.score_words.get(self.player1_score)
        player2_score_word = self.score_words.get(self.player2_score)
        return f"{player1_score_word}-{player2_score_word}"
