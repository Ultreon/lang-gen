from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.registry.BlockRendererRegistry as __BlockRendererRegistry
__BlockRendererRegistry = __BlockRendererRegistry
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.render.BlockRenderer as __BlockRenderer
__BlockRenderer = __BlockRenderer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BlockRendererRegistry():
    """dev.ultreon.quantum.client.registry.BlockRendererRegistry"""
 
    @staticmethod
    def __wrap(java_value: __BlockRendererRegistry) -> 'BlockRendererRegistry':
        return BlockRendererRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockRendererRegistry):
        """
        Dynamic initializer for BlockRendererRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def register(arg0: 'Block', arg1: 'BlockRenderer'):
        """public static void dev.ultreon.quantum.client.registry.BlockRendererRegistry.register(dev.ultreon.quantum.block.Block,dev.ultreon.quantum.client.render.BlockRenderer)"""
        __BlockRendererRegistry.register(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.registry.BlockRendererRegistry()"""
        val = __BlockRendererRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def get(arg0: 'Block') -> 'render.BlockRenderer':
        """public static dev.ultreon.quantum.client.render.BlockRenderer dev.ultreon.quantum.client.registry.BlockRendererRegistry.get(dev.ultreon.quantum.block.Block)"""
        return render.BlockRenderer.__wrap(__BlockRendererRegistry.get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.registry.BlockRendererRegistry()"""
        val = __BlockRendererRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.registry.BlockRendererRegistry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.registry.BlockRendererRegistry as __BlockRendererRegistry
__BlockRendererRegistry = __BlockRendererRegistry
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.render.BlockRenderer as __BlockRenderer
__BlockRenderer = __BlockRenderer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BlockRendererRegistry():
    """dev.ultreon.quantum.client.registry.BlockRendererRegistry"""
 
    @staticmethod
    def __wrap(java_value: __BlockRendererRegistry) -> 'BlockRendererRegistry':
        return BlockRendererRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockRendererRegistry):
        """
        Dynamic initializer for BlockRendererRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def register(arg0: 'Block', arg1: 'BlockRenderer'):
        """public static void dev.ultreon.quantum.client.registry.BlockRendererRegistry.register(dev.ultreon.quantum.block.Block,dev.ultreon.quantum.client.render.BlockRenderer)"""
        __BlockRendererRegistry.register(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.registry.BlockRendererRegistry()"""
        val = __BlockRendererRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def get(arg0: 'Block') -> 'render.BlockRenderer':
        """public static dev.ultreon.quantum.client.render.BlockRenderer dev.ultreon.quantum.client.registry.BlockRendererRegistry.get(dev.ultreon.quantum.block.Block)"""
        return render.BlockRenderer.__wrap(__BlockRendererRegistry.get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.registry.BlockRendererRegistry()"""
        val = __BlockRendererRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.registry.BlockRendererRegistry 
 
 
# CLASS: dev.ultreon.quantum.client.registry.MenuRegistry
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.registry.MenuRegistry as __MenuRegistry
__MenuRegistry = __MenuRegistry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.gui.screens import container
except ImportError:
    container = __import_once__("pyquantum.client.gui.screens.container")

import dev.ultreon.quantum.client.gui.screens.container.ContainerScreen as __ContainerScreen
__ContainerScreen = __ContainerScreen
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

from builtins import int
 
class MenuRegistry():
    """dev.ultreon.quantum.client.registry.MenuRegistry"""
 
    @staticmethod
    def __wrap(java_value: __MenuRegistry) -> 'MenuRegistry':
        return MenuRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MenuRegistry):
        """
        Dynamic initializer for MenuRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getScreen(arg0: 'ContainerMenu') -> 'container.ContainerScreen':
        """public static dev.ultreon.quantum.client.gui.screens.container.ContainerScreen dev.ultreon.quantum.client.registry.MenuRegistry.getScreen(dev.ultreon.quantum.menu.ContainerMenu)"""
        return container.ContainerScreen.__wrap(__MenuRegistry.getScreen(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.registry.MenuRegistry()"""
        val = __MenuRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def registerScreen(arg0: 'MenuType', arg1: 'ScreenBuilder'):
        """public static <T extends dev.ultreon.quantum.menu.ContainerMenu> void dev.ultreon.quantum.client.registry.MenuRegistry.registerScreen(dev.ultreon.quantum.menu.MenuType<T>,dev.ultreon.quantum.client.registry.MenuRegistry$ScreenBuilder<T>)"""
        __MenuRegistry.registerScreen(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.registry.MenuRegistry()"""
        val = __MenuRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.registry.LanguageRegistry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.registry.LanguageRegistry as __LanguageRegistry
__LanguageRegistry = __LanguageRegistry
import java.util.function.Consumer as Consumer
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LanguageRegistry():
    """dev.ultreon.quantum.client.registry.LanguageRegistry"""
 
    @staticmethod
    def __wrap(java_value: __LanguageRegistry) -> 'LanguageRegistry':
        return LanguageRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LanguageRegistry):
        """
        Dynamic initializer for LanguageRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def doRegistration(arg0: 'Consumer'):
        """public static void dev.ultreon.quantum.client.registry.LanguageRegistry.doRegistration(java.util.function.Consumer<dev.ultreon.quantum.util.Identifier>)"""
        __LanguageRegistry.doRegistration(arg0)

    @staticmethod
    @overload
    def register(arg0: 'Identifier'):
        """public static void dev.ultreon.quantum.client.registry.LanguageRegistry.register(dev.ultreon.quantum.util.Identifier)"""
        __LanguageRegistry.register(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.registry.LanguageRegistry()"""
        val = __LanguageRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.registry.LanguageRegistry()"""
        val = __LanguageRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.registry.ModIconOverrideRegistry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.client.registry.ModIconOverrideRegistry as __ModIconOverrideRegistry
__ModIconOverrideRegistry = __ModIconOverrideRegistry
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ModIconOverrideRegistry():
    """dev.ultreon.quantum.client.registry.ModIconOverrideRegistry"""
 
    @staticmethod
    def __wrap(java_value: __ModIconOverrideRegistry) -> 'ModIconOverrideRegistry':
        return ModIconOverrideRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModIconOverrideRegistry):
        """
        Dynamic initializer for ModIconOverrideRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def set(arg0: str, arg1: 'Identifier'):
        """public static void dev.ultreon.quantum.client.registry.ModIconOverrideRegistry.set(java.lang.String,dev.ultreon.quantum.util.Identifier)"""
        __ModIconOverrideRegistry.set(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.registry.ModIconOverrideRegistry()"""
        val = __ModIconOverrideRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.registry.ModIconOverrideRegistry()"""
        val = __ModIconOverrideRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def get(arg0: str) -> 'util.Identifier':
        """public static dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.registry.ModIconOverrideRegistry.get(java.lang.String)"""
        return util.Identifier.__wrap(__ModIconOverrideRegistry.get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.registry.BlockEntityModelRegistry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import dev.ultreon.quantum.client.model.block.BlockModel as __BlockModel
__BlockModel = __BlockModel
try:
    from pyquantum.client.model import block
except ImportError:
    block = __import_once__("pyquantum.client.model.block")

import java.lang.Long as __long
try:
    from pyquantum.block import entity
except ImportError:
    entity = __import_once__("pyquantum.block.entity")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.function.Function as Function
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.registry.BlockEntityModelRegistry as __BlockEntityModelRegistry
__BlockEntityModelRegistry = __BlockEntityModelRegistry
from builtins import int
 
class BlockEntityModelRegistry():
    """dev.ultreon.quantum.client.registry.BlockEntityModelRegistry"""
 
    @staticmethod
    def __wrap(java_value: __BlockEntityModelRegistry) -> 'BlockEntityModelRegistry':
        return BlockEntityModelRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockEntityModelRegistry):
        """
        Dynamic initializer for BlockEntityModelRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def register(arg0: 'BlockEntityType', arg1: 'Function'):
        """public static <T extends dev.ultreon.quantum.block.entity.BlockEntity> void dev.ultreon.quantum.client.registry.BlockEntityModelRegistry.register(dev.ultreon.quantum.block.entity.BlockEntityType<T>,java.util.function.Function<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.model.block.BlockModel>)"""
        __BlockEntityModelRegistry.register(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: 'BlockEntityType') -> 'block.BlockModel':
        """public static dev.ultreon.quantum.client.model.block.BlockModel dev.ultreon.quantum.client.registry.BlockEntityModelRegistry.get(dev.ultreon.quantum.block.entity.BlockEntityType<?>)"""
        return block.BlockModel.__wrap(__BlockEntityModelRegistry.get(arg0))

    @staticmethod
    @overload
    def load(arg0: 'QuantumClient'):
        """public static void dev.ultreon.quantum.client.registry.BlockEntityModelRegistry.load(dev.ultreon.quantum.client.QuantumClient)"""
        __BlockEntityModelRegistry.load(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.registry.EntityModelRegistry
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from builtins import type
import java.util.Map as __Map
__Map = __Map
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import java.util.Collection as Collection
import dev.ultreon.quantum.client.registry.EntityModelRegistry as __EntityModelRegistry
__EntityModelRegistry = __EntityModelRegistry
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = __import_once__("pygdx.assets.loaders")

import com.badlogic.gdx.graphics.g3d.Model as __Model
__Model = __Model
try:
    from pyquantum.client.model import entity
except ImportError:
    entity = __import_once__("pyquantum.client.model.entity")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import dev.ultreon.quantum.client.model.entity.EntityModel as __EntityModel
__EntityModel = __EntityModel
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class EntityModelRegistry():
    """dev.ultreon.quantum.client.registry.EntityModelRegistry"""
 
    @staticmethod
    def __wrap(java_value: __EntityModelRegistry) -> 'EntityModelRegistry':
        return EntityModelRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityModelRegistry):
        """
        Dynamic initializer for EntityModelRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self, arg0: 'EntityType') -> 'entity.EntityModel':
        """public <T extends dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.client.model.entity.EntityModel<T> dev.ultreon.quantum.client.registry.EntityModelRegistry.get(dev.ultreon.quantum.entity.EntityType<T>)"""
        return 'entity.EntityModel'.__wrap(super(__EntityModelRegistry, self).get(arg0))

    @overload
    def registerG3d(self, arg0: 'EntityType', arg1: 'Identifier'):
        """public <T extends dev.ultreon.quantum.entity.Entity> void dev.ultreon.quantum.client.registry.EntityModelRegistry.registerG3d(dev.ultreon.quantum.entity.EntityType<T>,dev.ultreon.quantum.util.Identifier)"""
        super(__EntityModelRegistry, self).registerG3d(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getAll(self) -> 'Collection':
        """public java.util.Collection<com.badlogic.gdx.graphics.g3d.Model> dev.ultreon.quantum.client.registry.EntityModelRegistry.getAll()"""
        return 'Collection'.__wrap(super(EntityModelRegistry, self).getAll())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.registry.EntityModelRegistry.dispose()"""
        super(EntityModelRegistry, self).dispose()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def registerBBModel(self, arg0: 'EntityType', arg1: 'Identifier'):
        """public <T extends dev.ultreon.quantum.entity.Entity> void dev.ultreon.quantum.client.registry.EntityModelRegistry.registerBBModel(dev.ultreon.quantum.entity.EntityType<T>,dev.ultreon.quantum.util.Identifier)"""
        super(__EntityModelRegistry, self).registerBBModel(arg0, arg1)

    @overload
    def getRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.entity.EntityType<?>, com.badlogic.gdx.graphics.g3d.Model> dev.ultreon.quantum.client.registry.EntityModelRegistry.getRegistry()"""
        return 'Map'.__wrap(super(EntityModelRegistry, self).getRegistry())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def registerFinished(self, arg0: 'EntityType', arg1: 'Model'):
        """public void dev.ultreon.quantum.client.registry.EntityModelRegistry.registerFinished(dev.ultreon.quantum.entity.EntityType<?>,com.badlogic.gdx.graphics.g3d.Model)"""
        super(__EntityModelRegistry, self).registerFinished(arg0, arg1)

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.registry.EntityModelRegistry.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(__EntityModelRegistry, self).reload(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def register(self, arg0: 'EntityType', arg1: 'EntityModel'):
        """public <T extends dev.ultreon.quantum.entity.Entity> void dev.ultreon.quantum.client.registry.EntityModelRegistry.register(dev.ultreon.quantum.entity.EntityType<T>,dev.ultreon.quantum.client.model.entity.EntityModel<T>)"""
        super(__EntityModelRegistry, self).register(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getFinished(self, arg0: 'EntityType') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.registry.EntityModelRegistry.getFinished(dev.ultreon.quantum.entity.EntityType<?>)"""
        return 'g3d.Model'.__wrap(super(__EntityModelRegistry, self).getFinished(arg0))

    @overload
    def __init__(self, arg0: 'ModelLoader', arg1: 'QuantumClient'):
        """public dev.ultreon.quantum.client.registry.EntityModelRegistry(com.badlogic.gdx.assets.loaders.ModelLoader<com.badlogic.gdx.assets.loaders.ModelLoader$ModelParameters>,dev.ultreon.quantum.client.QuantumClient)"""
        val = __EntityModelRegistry(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def registerGltf(self, arg0: 'EntityType', arg1: 'Identifier'):
        """public <T extends dev.ultreon.quantum.entity.Entity> void dev.ultreon.quantum.client.registry.EntityModelRegistry.registerGltf(dev.ultreon.quantum.entity.EntityType<T>,dev.ultreon.quantum.util.Identifier)"""
        super(__EntityModelRegistry, self).registerGltf(arg0, arg1) 
 
 
# CLASS: dev.ultreon.quantum.client.registry.EntityRendererRegistry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.model.entity import renderer
except ImportError:
    renderer = __import_once__("pyquantum.client.model.entity.renderer")

import java.util.function.BiFunction as BiFunction
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as __EntityRenderer
__EntityRenderer = __EntityRenderer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.registry.EntityRendererRegistry as __EntityRendererRegistry
__EntityRendererRegistry = __EntityRendererRegistry
from builtins import int
 
class EntityRendererRegistry():
    """dev.ultreon.quantum.client.registry.EntityRendererRegistry"""
 
    @staticmethod
    def __wrap(java_value: __EntityRendererRegistry) -> 'EntityRendererRegistry':
        return EntityRendererRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityRendererRegistry):
        """
        Dynamic initializer for EntityRendererRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'EntityModelRegistry'):
        """public dev.ultreon.quantum.client.registry.EntityRendererRegistry(dev.ultreon.quantum.client.registry.EntityModelRegistry)"""
        val = __EntityRendererRegistry(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self):
        """public void dev.ultreon.quantum.client.registry.EntityRendererRegistry.load()"""
        super(EntityRendererRegistry, self).load()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.registry.EntityRendererRegistry.dispose()"""
        super(EntityRendererRegistry, self).dispose()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.registry.EntityRendererRegistry.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(__EntityRendererRegistry, self).reload(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: 'EntityType') -> 'renderer.EntityRenderer':
        """public <T extends dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer<?> dev.ultreon.quantum.client.registry.EntityRendererRegistry.get(dev.ultreon.quantum.entity.EntityType<T>)"""
        return 'renderer.EntityRenderer'.__wrap(super(__EntityRendererRegistry, self).get(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def register(arg0: 'EntityType', arg1: 'BiFunction'):
        """public static <T extends dev.ultreon.quantum.entity.Entity,M extends dev.ultreon.quantum.client.model.entity.EntityModel<T>> void dev.ultreon.quantum.client.registry.EntityRendererRegistry.register(dev.ultreon.quantum.entity.EntityType<T>,java.util.function.BiFunction<M, com.badlogic.gdx.graphics.g3d.Model, dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer<T>>)"""
        __EntityRendererRegistry.register(arg0, arg1) 
 
 
# CLASS: dev.ultreon.quantum.client.registry.MenuRegistry$ScreenBuilder
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.registry.MenuRegistry as __MenuRegistry_ScreenBuilder
__ScreenBuilder = __MenuRegistry_ScreenBuilder.ScreenBuilder
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

from abc import abstractmethod, ABC
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

 
class ScreenBuilder(ABC):
    """dev.ultreon.quantum.client.registry.MenuRegistry.ScreenBuilder"""
 
    @staticmethod
    def __wrap(java_value: __ScreenBuilder) -> 'ScreenBuilder':
        return ScreenBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScreenBuilder):
        """
        Dynamic initializer for ScreenBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def build(self, arg0: 'ContainerMenu', arg1: 'TextObject'):
        """public abstract dev.ultreon.quantum.client.gui.screens.container.ContainerScreen dev.ultreon.quantum.client.registry.MenuRegistry$ScreenBuilder.build(T,dev.ultreon.quantum.text.TextObject)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.render.RenderLayer as __RenderLayer
__RenderLayer = __RenderLayer
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

import dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry as __BlockRenderTypeRegistry
__BlockRenderTypeRegistry = __BlockRenderTypeRegistry
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BlockRenderTypeRegistry():
    """dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry"""
 
    @staticmethod
    def __wrap(java_value: __BlockRenderTypeRegistry) -> 'BlockRenderTypeRegistry':
        return BlockRenderTypeRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockRenderTypeRegistry):
        """
        Dynamic initializer for BlockRenderTypeRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry()"""
        val = __BlockRenderTypeRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def get(arg0: 'Block') -> 'render.RenderLayer':
        """public static dev.ultreon.quantum.client.render.RenderLayer dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry.get(dev.ultreon.quantum.block.Block)"""
        return render.RenderLayer.__wrap(__BlockRenderTypeRegistry.get(arg0))

    @staticmethod
    @overload
    def register(arg0: 'Block', arg1: 'RenderLayer'):
        """public static void dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry.register(dev.ultreon.quantum.block.Block,dev.ultreon.quantum.client.render.RenderLayer)"""
        __BlockRenderTypeRegistry.register(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry()"""
        val = __BlockRenderTypeRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))