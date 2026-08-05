"""
User Routes Module

Handles HTTP endpoints for user management, including user registration,
profile updates, and retrieval.
"""

import logging

from flask import Blueprint, request, jsonify
from live_place_finder.models import user


LOGGER = logging.getLogger(__name__)

users_bp = Blueprint("users", __name__)



@users_bp.route("/api/users/<int:id>", methods=["GET"])
def get_user(id: int):


    try:
        user_data = user.get_users(id)

        if user_data is None:
            return (
                jsonify({
                "error": "user not found",
                "message": f"No user exists with id {id}"
            }), 404,)

        return jsonify(user_data), 200

    
    except Exception:
        LOGGER.exception("Failed to retrieve user with id=%s", id)

        return (
            jsonify(
                {
                    "error": "Internal Server Error",
                    "message": "An unexpected error occurred."
                }
            ),
            500,
        )

