from datetime import datetime, timedelta


class Token:
    def __init__(
        self,
        access_token: str,
        token_type: str,
        expires_in: int,
        refresh_token: str,
        scope: str,
        created_at: int,
    ):
        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.scope = scope
        if created_at:
            self.created_at = datetime.fromtimestamp(created_at)

    def is_access_token_expired(self):
        expiration_time = self.created_at + timedelta(seconds=self.expires_in)
        current_time = datetime.now()
        return current_time >= expiration_time

    def to_dict(self):
        return {
            "access_token": self.access_token,
            "token_type": self.token_type,
            "expires_in": self.expires_in,
            "refresh_token": self.refresh_token,
            "scope": self.scope,
            "created_at": self.created_at,
        }
