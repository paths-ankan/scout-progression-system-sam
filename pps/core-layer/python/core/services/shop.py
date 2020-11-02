import hashlib
import math
import time
from decimal import Decimal
from uuid import UUID

from core import ModelService
from core.db.model import Operator
from core.utils import join_key


class ShopService(ModelService):
    __table_name__ = "items"
    __partition_key__ = "category"
    __sort_key__ = "release-id"

    @classmethod
    def create(cls, name: str, description: str, price: int, category: str, release: int):
        index = cls.get_interface()

        ms_time = int(time.time() * 1e3)
        release_id = Decimal(release * 1e5 + ms_time % 1e5)

        item = {
            'name': name,
            'description': description,
            'price': price
        }
        return index.create(category, item, release_id, raise_if_exists_sort=True, raise_if_exists_partition=True)

    @classmethod
    def query(cls, category: str, release: int):
        index = cls.get_interface()
        return index.query(category, (Operator.LESS_THAN, int((release + 1) * 1e5)),
                           attributes=['name', 'category', 'description'])

    @classmethod
    def get(cls, category: str, release: int, id_: int):
        index = cls.get_interface()
        release_id = release * 100000 + id_
        return index.get(category, release_id, attributes=['name', 'category', 'description'])