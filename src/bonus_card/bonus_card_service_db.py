from .bonus_card_model import BonusCard
from flask import g
from typing import List


# CREATE
def create(code: str, price: float) -> BonusCard:
    bonus_card: BonusCard = BonusCard(
        owner_id=g.user_id,
        code=code,
        price=price)
    bonus_card.save_db()
    return bonus_card


# UPDATE
def update(bonus_card_id: int, code: str, price: float) -> BonusCard:
    bonus_card: BonusCard = BonusCard.query.filter_by(id=bonus_card_id).first()
    bonus_card.code = code
    bonus_card.price = price
    bonus_card.update_db()
    return bonus_card


# DELETE
def delete(bonus_card_id: int) -> BonusCard:
    bonus_card: BonusCard = BonusCard.query.filter_by(id=bonus_card_id).first()
    bonus_card.delete_db()
    return bonus_card


# GET BY ID
def get_by_id(bonus_card_id: int) -> BonusCard:
    bonus_card: BonusCard = BonusCard.query.filter_by(id=bonus_card_id, owner_id=g.user_id).first()
    return bonus_card


# GET BY KEY
def get_by_code(code: str) -> BonusCard:
    bonus_card: BonusCard = BonusCard.query.filter_by(code=code).first()
    return bonus_card


# GET ALL IDS
def get_all_ids() -> List[int]:
    bonus_cards: List[BonusCard] = BonusCard.query.filter_by(owner_id=g.user_id).all()
    bonus_card_ids: List[int] = []

    for bonus_card in bonus_cards:
        bonus_card_ids.append(bonus_card.id)

    return bonus_card_ids
