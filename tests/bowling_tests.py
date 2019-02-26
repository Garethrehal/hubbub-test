import unittest

import bowlingScores


class BowlingScoresTests(unittest.TestCase):

    def test_scoreIsNumberKnockedDown(self):
        self.assert_GameScore(4, [4])

    def test_gutterGame(self):
        self.assert_GameScore(0, [])

    def test_perfectGame(self):
        self.assert_GameScore(300, [10] * 12)

    def test_strikeIsTreatedAsTen(self):
        self.assert_GameScore(10, [10])

    def test_scoreAddsUpCorrectly(self):
        self.assert_GameScore(15, [4, 5, 3, 3])

    
    def test_stringInput(self):
        self.assertRaises(TypeError, bowlingScores.scoreGame(str("fffffff")), "Input must be of type list")

    def test_highInput(self):
        self.assertRaises(Exception, bowlingScores.scoreGame([14, 5, 3, 3]), "Score is impossibly high")   

    def test_lowInput(self):
        self.assertRaises(Exception, bowlingScores.scoreGame([-1, 5, 3, 3]), "Score is impossibly low")

    def test_decimalInput(self):
        self.assertRaises(TypeError, bowlingScores.scoreGame([0.32, 5, 3, 3]), "Scores must be intergers")
    

    def assert_GameScore(self, expected_score, game):
        self.assertEqual(expected_score, bowlingScores.scoreGame(game))




    
    
