from .loyal_card_model import LoyalCard
from flask import g
from typing import List


# CREATE
def create(code: str, price: float, full_name: str) -> LoyalCard:
    loyal_card: LoyalCard = LoyalCard(
        owner_id=g.user_id,
        code=code,
        price=price,
        full_name=full_name
    )
    loyal_card.save_db()
    return loyal_card


# UPDATE
def update(loyal_card_id: int, code: str, price: float, full_name: str) -> LoyalCard:
    loyal_card: LoyalCard = LoyalCard.query.filter_by(id=loyal_card_id).first()
    loyal_card.code = code
    loyal_card.price = price
    loyal_card.full_name = full_name
    loyal_card.update_db()
    return loyal_card


# DELETE
def delete(bonus_card_id: int) -> LoyalCard:
    loyal_card: LoyalCard = LoyalCard.query.filter_by(id=bonus_card_id).first()
    loyal_card.delete_db()
    return loyal_card


# GET BY ID
def get_by_id(loyal_card_id: int) -> LoyalCard:
    loyal_card: LoyalCard = LoyalCard.query.filter_by(id=loyal_card_id, owner_id=g.user_id).first()
    return loyal_card


# GET BY KEY
def get_by_code(code: str) -> LoyalCard:
    loyal_card: LoyalCard = LoyalCard.query.filter_by(code=code).first()
    return loyal_card


# GET ALL IDS
def get_all_ids() -> List[int]:
    loyal_cards: List[LoyalCard] = LoyalCard.query.filter_by(owner_id=g.user_id).all()
    loyal_card_ids: List[int] = []

    for loyal_card in loyal_cards:
        loyal_card_ids.append(loyal_card.id)

    return loyal_card_ids
