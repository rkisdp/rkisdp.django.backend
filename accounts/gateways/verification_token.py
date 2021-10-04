# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals
from contextlib import suppress
from typing import Optional

# project imports
from accounts.models import VerificationToken as VerificationTokenModel


def create_verification_token(
    data: dict
) -> VerificationTokenModel:
    """
    Save a Verification Token instance to database.

    Args:
        data (dictionary):

    Returns:
        VerificationToken:
            Verification Token entity of VerificationTokenModel object

    Raises:
        None
    """
    orm_verification_token = VerificationTokenModel(
        user_id=data.get('user_id'),
        token_type=data.get('token_type', 'SMS'),
        token=True
    )
    orm_verification_token.save()
    return orm_verification_token


def update_verification_token(
    pk: int,
    data: dict
) -> VerificationTokenModel:
    """
    Update Verification Token instance by primary Key

    Args:
        pk: int
        data: dictionary

    Returns:
        :obj: VerificationToken:
            VerificationToken entity of VerificationTokenModel object

    Raises:
        None
    """
    verification_token = VerificationTokenModel.objects.get(
        id=pk
    )
    verification_token.is_valid = verification_token_entity.is_valid
    verification_token.number_attempts = (
        verification_token_entity.number_attempts
    )
    verification_token.save()
    return verification_token


def get_user_valid_token(
    user_id: int, token_type: str
) -> Optional[VerificationTokenModel]:
    """
    Filter User Valid Token for token type

    Args:
        user_id (int): user_id of which we need to filter verification tokens
        token_type (str): token_type can be email or sms

    Returns:
        :obj: VerificationToken:
            VerificationToken entity of VerificationTokenModel object

    Raise:
        None
    """
    orm_verification_token = (
        VerificationTokenModel.objects.filter_user(user_id=user_id)
        .filter_token_type(token_type=token_type)
        .filter_valid()
        .till_attempt()
    )
    if orm_verification_token.last():
        return orm_verification_token.last()
    return None


def get_verification_token(pk: int):
    with suppress(VerificationTokenModel.DoesNotExist):
        return VerificationTokenModel.objects.get(pk=pk)
    return None
