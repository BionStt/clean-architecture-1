from datetime import datetime, timedelta
from typing import List, Optional

from foundation.value_objects.factories import get_dollars

from auctions.domain.entities import Auction, Bid
from auctions.domain.types import AuctionId


def create_auction(
    auction_id: AuctionId = 1, bids: Optional[List[Bid]] = None, ends_at: Optional[datetime] = None, ended: bool = False
) -> Auction:
    if not bids:
        bids = []

    if not ends_at:
        ends_at = datetime.now() + timedelta(days=1)

    return Auction(
        id=auction_id, title="", starting_price=get_dollars("10.00"), bids=bids, ends_at=ends_at, ended=ended
    )
