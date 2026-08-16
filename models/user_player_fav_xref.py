from db import db

users_players_fav_table = db.Table(
    "UsersPlayersfav",
    db.Model.metadata,
    db.Column("user_id", db.ForeignKey("Users.user_id", ondelete="CASCADE"), primary_key=True),
    db.Column("player_id", db.ForeignKey("Players.player_id", ondelete="CASCADE"), primary_key=True)
)