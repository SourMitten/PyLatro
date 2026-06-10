#!/usr/bin/env python3
"""Test poker hand evaluation against Lua source values"""

import sys
sys.path.insert(0, '/workspaces/PyLatro')

from balatro_py.core.card import Card
from balatro_py.core.poker_hands import PokerHandEvaluator, PokerHandType

def test_poker_hands():
    """Test poker hand evaluation with exact Lua values"""
    
    print("🧪 Testing Poker Hand Evaluation Against Lua Source...\n")
    
    tests = [
        # (description, cards_data, expected_hand_type, expected_chips, expected_mult)
        (
            "High Card",
            [("Spades", "A"), ("Diamonds", "Q"), ("Diamonds", "9"), ("Clubs", "4"), ("Diamonds", "3")],
            PokerHandType.HIGH_CARD,
            5, 1
        ),
        (
            "Pair",
            [("Spades", "9"), ("Hearts", "9"), ("Hearts", "6"), ("Diamonds", "6"), ("Diamonds", "3")],
            PokerHandType.PAIR,
            10, 2
        ),
        (
            "Two Pair",
            [("Hearts", "A"), ("Diamonds", "A"), ("Hearts", "4"), ("Clubs", "4"), ("Diamonds", "Q")],
            PokerHandType.TWO_PAIR,
            20, 2
        ),
        (
            "Three of a Kind",
            [("Spades", "10"), ("Clubs", "10"), ("Diamonds", "10"), ("Hearts", "6"), ("Diamonds", "5")],
            PokerHandType.THREE_OF_A_KIND,
            30, 3
        ),
        (
            "Straight",
            [("Diamonds", "J"), ("Clubs", "10"), ("Clubs", "9"), ("Spades", "8"), ("Hearts", "7")],
            PokerHandType.STRAIGHT,
            30, 4
        ),
        (
            "Flush",
            [("Hearts", "A"), ("Hearts", "K"), ("Hearts", "10"), ("Hearts", "5"), ("Hearts", "4")],
            PokerHandType.FLUSH,
            35, 4
        ),
        (
            "Full House",
            [("Hearts", "K"), ("Clubs", "K"), ("Diamonds", "K"), ("Spades", "2"), ("Diamonds", "2")],
            PokerHandType.FULL_HOUSE,
            40, 4
        ),
        (
            "Four of a Kind",
            [("Spades", "J"), ("Hearts", "J"), ("Clubs", "J"), ("Diamonds", "J"), ("Clubs", "3")],
            PokerHandType.FOUR_OF_A_KIND,
            60, 7
        ),
        (
            "Straight Flush",
            [("Spades", "Q"), ("Spades", "J"), ("Spades", "10"), ("Spades", "9"), ("Spades", "8")],
            PokerHandType.STRAIGHT_FLUSH,
            100, 8
        ),
    ]
    
    passed = 0
    failed = 0
    
    for description, cards_data, expected_type, expected_chips, expected_mult in tests:
        # Create cards (Card takes suit, rank)
        cards = [Card(suit, rank) for suit, rank in cards_data]
        
        # Evaluate
        hand_type, scoring_cards = PokerHandEvaluator.evaluate_hand(cards)
        actual_chips = hand_type.get_base_chips()
        actual_mult = hand_type.get_base_mult()
        
        # Check results
        type_match = hand_type == expected_type
        chips_match = actual_chips == expected_chips
        mult_match = actual_mult == expected_mult
        
        status = "✅ PASS" if (type_match and chips_match and mult_match) else "❌ FAIL"
        
        print(f"{status} | {description:20} | Expected: {expected_type.name:18} (chips={expected_chips}, mult={expected_mult})")
        if not type_match:
            print(f"       | Got: {hand_type.name:18} (chips={actual_chips}, mult={actual_mult})")
        
        if type_match and chips_match and mult_match:
            passed += 1
        else:
            failed += 1
    
    print(f"\n📊 Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("✅ All tests passed! Lua accuracy verified!")
        return True
    else:
        print("❌ Some tests failed. Review implementation.")
        return False

if __name__ == "__main__":
    success = test_poker_hands()
    sys.exit(0 if success else 1)
