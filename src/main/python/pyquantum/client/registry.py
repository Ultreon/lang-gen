from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.registry.BlockRendererRegistry as _BlockRendererRegistry
_BlockRendererRegistry = _BlockRendererRegistry
try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.render.BlockRenderer as _BlockRenderer
_BlockRenderer = _BlockRenderer
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockRendererRegistry():
    """dev.ultreon.quantum.client.registry.BlockRendererRegistry"""
 
    @staticmethod
    def _wrap(java_value: _BlockRendererRegistry) -> 'BlockRendererRegistry':
        return BlockRendererRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockRendererRegistry):
        """
        Dynamic initializer for BlockRendererRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockRendererRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockRendererRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.registry.BlockRendererRegistry()"""
        val = _BlockRendererRegistry()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.registry.BlockRendererRegistry()"""
        val = _BlockRendererRegistry()
        self.__wrapper = val

    @staticmethod
    @overload
    def get(arg0: 'Block') -> 'render.BlockRenderer':
        """public static dev.ultreon.quantum.client.render.BlockRenderer dev.ultreon.quantum.client.registry.BlockRendererRegistry.get(dev.ultreon.quantum.block.Block)"""
        return render.BlockRenderer._wrap(_BlockRendererRegistry.get(arg0))

    @staticmethod
    @overload
    def register(arg0: 'Block', arg1: 'BlockRenderer'):
        """public static void dev.ultreon.quantum.client.registry.BlockRendererRegistry.register(dev.ultreon.quantum.block.Block,dev.ultreon.quantum.client.render.BlockRenderer)"""
        _BlockRendererRegistry.register(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.registry.BlockRendererRegistry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.registry.BlockRendererRegistry as _BlockRendererRegistry
_BlockRendererRegistry = _BlockRendererRegistry
try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.render.BlockRenderer as _BlockRenderer
_BlockRenderer = _BlockRenderer
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockRendererRegistry():
    """dev.ultreon.quantum.client.registry.BlockRendererRegistry"""
 
    @staticmethod
    def _wrap(java_value: _BlockRendererRegistry) -> 'BlockRendererRegistry':
        return BlockRendererRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockRendererRegistry):
        """
        Dynamic initializer for BlockRendererRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockRendererRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockRendererRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.registry.BlockRendererRegistry()"""
        val = _BlockRendererRegistry()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.registry.BlockRendererRegistry()"""
        val = _BlockRendererRegistry()
        self.__wrapper = val

    @staticmethod
    @overload
    def get(arg0: 'Block') -> 'render.BlockRenderer':
        """public static dev.ultreon.quantum.client.render.BlockRenderer dev.ultreon.quantum.client.registry.BlockRendererRegistry.get(dev.ultreon.quantum.block.Block)"""
        return render.BlockRenderer._wrap(_BlockRendererRegistry.get(arg0))

    @staticmethod
    @overload
    def register(arg0: 'Block', arg1: 'BlockRenderer'):
        """public static void dev.ultreon.quantum.client.registry.BlockRendererRegistry.register(dev.ultreon.quantum.block.Block,dev.ultreon.quantum.client.render.BlockRenderer)"""
        _BlockRendererRegistry.register(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.registry.BlockRendererRegistry 
 
 
# CLASS: dev.ultreon.quantum.client.registry.MenuRegistry
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.client.gui.screens.container.ContainerScreen as _ContainerScreen
_ContainerScreen = _ContainerScreen
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.registry.MenuRegistry as _MenuRegistry
_MenuRegistry = _MenuRegistry
try:
    from pyquantum.client.gui.screens import container
except ImportError:
    container = _import_once("pyquantum.client.gui.screens.container")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MenuRegistry():
    """dev.ultreon.quantum.client.registry.MenuRegistry"""
 
    @staticmethod
    def _wrap(java_value: _MenuRegistry) -> 'MenuRegistry':
        return MenuRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MenuRegistry):
        """
        Dynamic initializer for MenuRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MenuRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MenuRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getScreen(arg0: 'ContainerMenu') -> 'container.ContainerScreen':
        """public static dev.ultreon.quantum.client.gui.screens.container.ContainerScreen dev.ultreon.quantum.client.registry.MenuRegistry.getScreen(dev.ultreon.quantum.menu.ContainerMenu)"""
        return container.ContainerScreen._wrap(_MenuRegistry.getScreen(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.registry.MenuRegistry()"""
        val = _MenuRegistry()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def registerScreen(arg0: 'MenuType', arg1: 'ScreenBuilder'):
        """public static <T extends dev.ultreon.quantum.menu.ContainerMenu> void dev.ultreon.quantum.client.registry.MenuRegistry.registerScreen(dev.ultreon.quantum.menu.MenuType<T>,dev.ultreon.quantum.client.registry.MenuRegistry$ScreenBuilder<T>)"""
        _MenuRegistry.registerScreen(arg0, arg1)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.registry.MenuRegistry()"""
        val = _MenuRegistry()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.registry.LanguageRegistry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.client.registry.LanguageRegistry as _LanguageRegistry
_LanguageRegistry = _LanguageRegistry
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LanguageRegistry():
    """dev.ultreon.quantum.client.registry.LanguageRegistry"""
 
    @staticmethod
    def _wrap(java_value: _LanguageRegistry) -> 'LanguageRegistry':
        return LanguageRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LanguageRegistry):
        """
        Dynamic initializer for LanguageRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LanguageRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LanguageRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def doRegistration(arg0: 'Consumer'):
        """public static void dev.ultreon.quantum.client.registry.LanguageRegistry.doRegistration(java.util.function.Consumer<dev.ultreon.quantum.util.Identifier>)"""
        _LanguageRegistry.doRegistration(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.registry.LanguageRegistry()"""
        val = _LanguageRegistry()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def register(arg0: 'Identifier'):
        """public static void dev.ultreon.quantum.client.registry.LanguageRegistry.register(dev.ultreon.quantum.util.Identifier)"""
        _LanguageRegistry.register(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.registry.LanguageRegistry()"""
        val = _LanguageRegistry()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.registry.ModIconOverrideRegistry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.registry.ModIconOverrideRegistry as _ModIconOverrideRegistry
_ModIconOverrideRegistry = _ModIconOverrideRegistry
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModIconOverrideRegistry():
    """dev.ultreon.quantum.client.registry.ModIconOverrideRegistry"""
 
    @staticmethod
    def _wrap(java_value: _ModIconOverrideRegistry) -> 'ModIconOverrideRegistry':
        return ModIconOverrideRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModIconOverrideRegistry):
        """
        Dynamic initializer for ModIconOverrideRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModIconOverrideRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModIconOverrideRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def set(arg0: str, arg1: 'Identifier'):
        """public static void dev.ultreon.quantum.client.registry.ModIconOverrideRegistry.set(java.lang.String,dev.ultreon.quantum.util.Identifier)"""
        _ModIconOverrideRegistry.set(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def get(arg0: str) -> 'util.Identifier':
        """public static dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.registry.ModIconOverrideRegistry.get(java.lang.String)"""
        return util.Identifier._wrap(_ModIconOverrideRegistry.get(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.registry.ModIconOverrideRegistry()"""
        val = _ModIconOverrideRegistry()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.registry.ModIconOverrideRegistry()"""
        val = _ModIconOverrideRegistry()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.registry.BlockEntityModelRegistry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.registry.BlockEntityModelRegistry as _BlockEntityModelRegistry
_BlockEntityModelRegistry = _BlockEntityModelRegistry
try:
    from pyquantum.client.model import block
except ImportError:
    block = _import_once("pyquantum.client.model.block")

try:
    from pyquantum.block import entity
except ImportError:
    entity = _import_once("pyquantum.block.entity")

import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.block.BlockModel as _BlockModel
_BlockModel = _BlockModel
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockEntityModelRegistry():
    """dev.ultreon.quantum.client.registry.BlockEntityModelRegistry"""
 
    @staticmethod
    def _wrap(java_value: _BlockEntityModelRegistry) -> 'BlockEntityModelRegistry':
        return BlockEntityModelRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockEntityModelRegistry):
        """
        Dynamic initializer for BlockEntityModelRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockEntityModelRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockEntityModelRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def get(arg0: 'BlockEntityType') -> 'block.BlockModel':
        """public static dev.ultreon.quantum.client.model.block.BlockModel dev.ultreon.quantum.client.registry.BlockEntityModelRegistry.get(dev.ultreon.quantum.block.entity.BlockEntityType<?>)"""
        return block.BlockModel._wrap(_BlockEntityModelRegistry.get(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def register(arg0: 'BlockEntityType', arg1: 'Function'):
        """public static <T extends dev.ultreon.quantum.block.entity.BlockEntity> void dev.ultreon.quantum.client.registry.BlockEntityModelRegistry.register(dev.ultreon.quantum.block.entity.BlockEntityType<T>,java.util.function.Function<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.model.block.BlockModel>)"""
        _BlockEntityModelRegistry.register(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def load(arg0: 'QuantumClient'):
        """public static void dev.ultreon.quantum.client.registry.BlockEntityModelRegistry.load(dev.ultreon.quantum.client.QuantumClient)"""
        _BlockEntityModelRegistry.load(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.registry.EntityModelRegistry
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.util.Collection as Collection
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

try:
    from pyquantum.client.model import entity
except ImportError:
    entity = _import_once("pyquantum.client.model.entity")

from builtins import bool
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
import dev.ultreon.quantum.client.registry.EntityModelRegistry as _EntityModelRegistry
_EntityModelRegistry = _EntityModelRegistry
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.client.model.entity.EntityModel as _EntityModel
_EntityModel = _EntityModel
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntityModelRegistry():
    """dev.ultreon.quantum.client.registry.EntityModelRegistry"""
 
    @staticmethod
    def _wrap(java_value: _EntityModelRegistry) -> 'EntityModelRegistry':
        return EntityModelRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityModelRegistry):
        """
        Dynamic initializer for EntityModelRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityModelRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityModelRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getAll(self) -> 'Collection':
        """public java.util.Collection<com.badlogic.gdx.graphics.g3d.Model> dev.ultreon.quantum.client.registry.EntityModelRegistry.getAll()"""
        return 'Collection'._wrap(super(EntityModelRegistry, self).getAll())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def registerFinished(self, arg0: 'EntityType', arg1: 'Model'):
        """public void dev.ultreon.quantum.client.registry.EntityModelRegistry.registerFinished(dev.ultreon.quantum.entity.EntityType<?>,com.badlogic.gdx.graphics.g3d.Model)"""
        super(_EntityModelRegistry, self).registerFinished(arg0, arg1)

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

    @overload
    def registerGltf(self, arg0: 'EntityType', arg1: 'Identifier'):
        """public <T extends dev.ultreon.quantum.entity.Entity> void dev.ultreon.quantum.client.registry.EntityModelRegistry.registerGltf(dev.ultreon.quantum.entity.EntityType<T>,dev.ultreon.quantum.util.Identifier)"""
        super(_EntityModelRegistry, self).registerGltf(arg0, arg1)

    @overload
    def registerBBModel(self, arg0: 'EntityType', arg1: 'Identifier'):
        """public <T extends dev.ultreon.quantum.entity.Entity> void dev.ultreon.quantum.client.registry.EntityModelRegistry.registerBBModel(dev.ultreon.quantum.entity.EntityType<T>,dev.ultreon.quantum.util.Identifier)"""
        super(_EntityModelRegistry, self).registerBBModel(arg0, arg1)

    @overload
    def __init__(self, arg0: 'ModelLoader', arg1: 'QuantumClient'):
        """public dev.ultreon.quantum.client.registry.EntityModelRegistry(com.badlogic.gdx.assets.loaders.ModelLoader<com.badlogic.gdx.assets.loaders.ModelLoader$ModelParameters>,dev.ultreon.quantum.client.QuantumClient)"""
        val = _EntityModelRegistry(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.registry.EntityModelRegistry.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(_EntityModelRegistry, self).reload(arg0, arg1)

    @overload
    def getFinished(self, arg0: 'EntityType') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.registry.EntityModelRegistry.getFinished(dev.ultreon.quantum.entity.EntityType<?>)"""
        return 'g3d.Model'._wrap(super(_EntityModelRegistry, self).getFinished(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def register(self, arg0: 'EntityType', arg1: 'EntityModel'):
        """public <T extends dev.ultreon.quantum.entity.Entity> void dev.ultreon.quantum.client.registry.EntityModelRegistry.register(dev.ultreon.quantum.entity.EntityType<T>,dev.ultreon.quantum.client.model.entity.EntityModel<T>)"""
        super(_EntityModelRegistry, self).register(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def registerG3d(self, arg0: 'EntityType', arg1: 'Identifier'):
        """public <T extends dev.ultreon.quantum.entity.Entity> void dev.ultreon.quantum.client.registry.EntityModelRegistry.registerG3d(dev.ultreon.quantum.entity.EntityType<T>,dev.ultreon.quantum.util.Identifier)"""
        super(_EntityModelRegistry, self).registerG3d(arg0, arg1)

    @overload
    def getRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.entity.EntityType<?>, com.badlogic.gdx.graphics.g3d.Model> dev.ultreon.quantum.client.registry.EntityModelRegistry.getRegistry()"""
        return 'Map'._wrap(super(EntityModelRegistry, self).getRegistry())

    @overload
    def get(self, arg0: 'EntityType') -> 'entity.EntityModel':
        """public <T extends dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.client.model.entity.EntityModel<T> dev.ultreon.quantum.client.registry.EntityModelRegistry.get(dev.ultreon.quantum.entity.EntityType<T>)"""
        return 'entity.EntityModel'._wrap(super(_EntityModelRegistry, self).get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.registry.EntityRendererRegistry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.registry.EntityRendererRegistry as _EntityRendererRegistry
_EntityRendererRegistry = _EntityRendererRegistry
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client.model.entity import renderer
except ImportError:
    renderer = _import_once("pyquantum.client.model.entity.renderer")

import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as _EntityRenderer
_EntityRenderer = _EntityRenderer
import java.lang.Integer as _int
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntityRendererRegistry():
    """dev.ultreon.quantum.client.registry.EntityRendererRegistry"""
 
    @staticmethod
    def _wrap(java_value: _EntityRendererRegistry) -> 'EntityRendererRegistry':
        return EntityRendererRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityRendererRegistry):
        """
        Dynamic initializer for EntityRendererRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityRendererRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityRendererRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def register(arg0: 'EntityType', arg1: 'BiFunction'):
        """public static <T extends dev.ultreon.quantum.entity.Entity,M extends dev.ultreon.quantum.client.model.entity.EntityModel<T>> void dev.ultreon.quantum.client.registry.EntityRendererRegistry.register(dev.ultreon.quantum.entity.EntityType<T>,java.util.function.BiFunction<M, com.badlogic.gdx.graphics.g3d.Model, dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer<T>>)"""
        _EntityRendererRegistry.register(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.registry.EntityRendererRegistry.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(_EntityRendererRegistry, self).reload(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.registry.EntityRendererRegistry.dispose()"""
        super(EntityRendererRegistry, self).dispose()

    @overload
    def __init__(self, arg0: 'EntityModelRegistry'):
        """public dev.ultreon.quantum.client.registry.EntityRendererRegistry(dev.ultreon.quantum.client.registry.EntityModelRegistry)"""
        val = _EntityRendererRegistry(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: 'EntityType') -> 'renderer.EntityRenderer':
        """public <T extends dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer<?> dev.ultreon.quantum.client.registry.EntityRendererRegistry.get(dev.ultreon.quantum.entity.EntityType<T>)"""
        return 'renderer.EntityRenderer'._wrap(super(_EntityRendererRegistry, self).get(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.registry.MenuRegistry$ScreenBuilder
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.registry.MenuRegistry as _MenuRegistry_ScreenBuilder
_ScreenBuilder = _MenuRegistry_ScreenBuilder.ScreenBuilder
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

from abc import abstractmethod, ABC
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

 
class ScreenBuilder():
    """dev.ultreon.quantum.client.registry.MenuRegistry.ScreenBuilder"""
 
    @staticmethod
    def _wrap(java_value: _ScreenBuilder) -> 'ScreenBuilder':
        return ScreenBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScreenBuilder):
        """
        Dynamic initializer for ScreenBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScreenBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScreenBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def build(self, arg0: 'ContainerMenu', arg1: 'TextObject'):
        """public abstract dev.ultreon.quantum.client.gui.screens.container.ContainerScreen dev.ultreon.quantum.client.registry.MenuRegistry$ScreenBuilder.build(T,dev.ultreon.quantum.text.TextObject)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry as _BlockRenderTypeRegistry
_BlockRenderTypeRegistry = _BlockRenderTypeRegistry
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.render.RenderLayer as _RenderLayer
_RenderLayer = _RenderLayer
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockRenderTypeRegistry():
    """dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry"""
 
    @staticmethod
    def _wrap(java_value: _BlockRenderTypeRegistry) -> 'BlockRenderTypeRegistry':
        return BlockRenderTypeRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockRenderTypeRegistry):
        """
        Dynamic initializer for BlockRenderTypeRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockRenderTypeRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockRenderTypeRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def register(arg0: 'Block', arg1: 'RenderLayer'):
        """public static void dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry.register(dev.ultreon.quantum.block.Block,dev.ultreon.quantum.client.render.RenderLayer)"""
        _BlockRenderTypeRegistry.register(arg0, arg1)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry()"""
        val = _BlockRenderTypeRegistry()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry()"""
        val = _BlockRenderTypeRegistry()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def get(arg0: 'Block') -> 'render.RenderLayer':
        """public static dev.ultreon.quantum.client.render.RenderLayer dev.ultreon.quantum.client.registry.BlockRenderTypeRegistry.get(dev.ultreon.quantum.block.Block)"""
        return render.RenderLayer._wrap(_BlockRenderTypeRegistry.get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())