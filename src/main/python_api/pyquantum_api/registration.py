from pyquantum.block import Block
from pyquantum.item import BlockItem, Item, Item_Properties

from pyquantum_api.constants import MOD_ID


class Blocks:
    from pyquantum.registry import DeferRegistry
    from pyquantum.registry import DeferredElement
    from pyquantum.registry import Registries
    from jlang import Thread

    Thread()

    @staticmethod
    def init():
        Blocks.REGISTER.register()

    REGISTER: DeferRegistry = DeferRegistry.of(MOD_ID, Registries.BLOCK)

    EXAMPLE_BLOCK: DeferredElement = REGISTER.defer("example_block", lambda: Block())

    REGISTER.register()


class Items:
    from pyquantum.registry import DeferRegistry
    from pyquantum.registry import DeferredElement
    from pyquantum.registry import Registries

    @staticmethod
    def init():
        Items.REGISTER.register()

    REGISTER: DeferRegistry = DeferRegistry.of(MOD_ID, Registries.ITEM)

    EXAMPLE_ITEM: DeferredElement = REGISTER.defer(
        "example_item", lambda: BlockItem(Item_Properties(), lambda: Blocks.EXAMPLE_BLOCK.get())
    )

    REGISTER.register()


def init():
    Blocks.init()
    Items.init()
