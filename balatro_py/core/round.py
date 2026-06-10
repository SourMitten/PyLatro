"""Round management system"""

from typing import Optional, List, Tuple
from .hand import Hand
from .deck import Deck
from .scoring import Scoring
from .poker_hands import PokerHandType


class Round:
    """Manages a single round of gameplay"""

    def __init__(self, target_score: int = 300):
        """Initialize a round"""
        self.hand = Hand()
        self.deck = Deck()
        self.deck.shuffle()
        self.scoring = Scoring()
        
        self.hands_left = 5
        self.discards_left = 3
        self.current_hand_score = 0
        self.round_score = 0
        self.target_score = target_score
        
        self.played_hands: List[Tuple[PokerHandType, int]] = []
        self.round_complete = False
        self.round_won = False

    def draw_cards(self, num_cards: int = 5) -> List:
        """Draw cards from deck"""
        cards = self.deck.draw(num_cards)
        for card in cards:
            self.hand.add_card(card)
        return cards

    def play_hand(self, jokers: List = None) -> int:
        """
        Play the current hand and return the score.
        
        Args:
            jokers: List of active jokers
            
        Returns:
            The score achieved
        """
        if self.hands_left <= 0:
            return 0

        hand_type, scoring_cards, chips, mult, score = self.hand.evaluate()
        
        # Apply joker effects
        joker_chips = 0
        joker_mult = 1.0
        if jokers:
            for joker in jokers:
                if joker.active:
                    j_chips, j_mult = joker.calculate_effect(scoring_cards)
                    joker_chips += j_chips
                    joker_mult *= j_mult
                    joker.on_play(scoring_cards)

        final_chips = chips + joker_chips
        final_score = int(final_chips * mult * joker_mult)

        self.current_hand_score = final_score
        self.round_score += final_score
        self.hands_left -= 1
        self.played_hands.append((hand_type, final_score))

        # Remove played cards from hand
        for card in scoring_cards:
            self.hand.remove_card(card)

        # Check if round is won
        if self.round_score >= self.target_score:
            self.round_complete = True
            self.round_won = True

        return final_score

    def discard(self) -> bool:
        """
        Perform a discard action.
        
        Returns:
            True if discard was successful
        """
        if self.discards_left <= 0:
            return False

        selected = self.hand.get_selected_cards()
        if not selected:
            return False

        for card in selected:
            self.hand.remove_card(card)

        self.discards_left -= 1
        self.hand.clear_selection()
        
        # Draw replacement cards
        self.draw_cards(len(selected))
        
        return True

    def check_round_complete(self) -> bool:
        """
        Check if the round is complete (won or lost).
        
        Returns:
            True if round is over
        """
        if self.round_complete:
            return True
        
        # Lose if out of hands and haven't won
        if self.hands_left <= 0 and self.round_score < self.target_score:
            self.round_complete = True
            self.round_won = False
            return True
        
        return False

    def get_status(self) -> str:
        """Get current round status"""
        return f"Score: {self.round_score}/{self.target_score} | Hands: {self.hands_left} | Discards: {self.discards_left}"

    def reset(self):
        """Reset round values"""
        self.hand.clear()
        self.deck = Deck()
        self.deck.shuffle()
        self.hands_left = 5
        self.discards_left = 3
        self.current_hand_score = 0
        self.round_score = 0
        self.played_hands.clear()
        self.round_complete = False
        self.round_won = False
