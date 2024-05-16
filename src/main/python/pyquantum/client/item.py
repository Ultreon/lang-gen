from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.client.item.ItemRenderer as __ItemRenderer
__ItemRenderer = __ItemRenderer
import com.badlogic.gdx.graphics.g3d.ModelInstance as __ModelInstance
__ModelInstance = __ModelInstance
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

try:
    from pyquantum.client.model import item
except ImportError:
    item = __import_once__("pyquantum.client.model.item")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

try:
    from pyquantum.client.model import model
except ImportError:
    model = __import_once__("pyquantum.client.model.model")

import com.badlogic.gdx.graphics.OrthographicCamera as __OrthographicCamera
__OrthographicCamera = __OrthographicCamera
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class ItemRenderer():
    """dev.ultreon.quantum.client.item.ItemRenderer"""
 
    @staticmethod
    def __wrap(java_value: __ItemRenderer) -> 'ItemRenderer':
        return ItemRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ItemRenderer):
        """
        Dynamic initializer for ItemRenderer.
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
    def registerBlockModel(self, arg0: 'BlockItem', arg1: 'Supplier'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.registerBlockModel(dev.ultreon.quantum.item.BlockItem,java.util.function.Supplier<dev.ultreon.quantum.client.model.block.BlockModel>)"""
        super(__ItemRenderer, self).registerBlockModel(arg0, arg1)

    @overload
    def reload(self):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.reload()"""
        super(ItemRenderer, self).reload()

    @overload
    def registerModel(self, arg0: 'Item', arg1: 'ItemModel'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.registerModel(dev.ultreon.quantum.item.Item,dev.ultreon.quantum.client.model.item.ItemModel)"""
        super(__ItemRenderer, self).registerModel(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def render(self, arg0: 'Item', arg1: 'Renderer', arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.render(dev.ultreon.quantum.item.Item,dev.ultreon.quantum.client.gui.Renderer,int,int)"""
        super(__ItemRenderer, self).render(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getItemCam(self) -> 'graphics.OrthographicCamera':
        """public com.badlogic.gdx.graphics.OrthographicCamera dev.ultreon.quantum.client.item.ItemRenderer.getItemCam()"""
        return 'graphics.OrthographicCamera'.__wrap(super(ItemRenderer, self).getItemCam())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.dispose()"""
        super(ItemRenderer, self).dispose()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def registerModels(self, arg0: 'Json5ModelLoader'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.registerModels(dev.ultreon.quantum.client.model.model.Json5ModelLoader)"""
        super(__ItemRenderer, self).registerModels(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def loadModels(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.loadModels(dev.ultreon.quantum.client.QuantumClient)"""
        super(__ItemRenderer, self).loadModels(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def createModelInstance(self, arg0: 'ItemStack') -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.item.ItemRenderer.createModelInstance(dev.ultreon.quantum.item.ItemStack)"""
        return 'g3d.ModelInstance'.__wrap(super(__ItemRenderer, self).createModelInstance(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.resize(int,int)"""
        super(__ItemRenderer, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.item.ItemRenderer(dev.ultreon.quantum.client.QuantumClient)"""
        val = __ItemRenderer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.client.item.ItemRenderer
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.client.item.ItemRenderer as __ItemRenderer
__ItemRenderer = __ItemRenderer
import com.badlogic.gdx.graphics.g3d.ModelInstance as __ModelInstance
__ModelInstance = __ModelInstance
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

try:
    from pyquantum.client.model import item
except ImportError:
    item = __import_once__("pyquantum.client.model.item")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

try:
    from pyquantum.client.model import model
except ImportError:
    model = __import_once__("pyquantum.client.model.model")

import com.badlogic.gdx.graphics.OrthographicCamera as __OrthographicCamera
__OrthographicCamera = __OrthographicCamera
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class ItemRenderer():
    """dev.ultreon.quantum.client.item.ItemRenderer"""
 
    @staticmethod
    def __wrap(java_value: __ItemRenderer) -> 'ItemRenderer':
        return ItemRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ItemRenderer):
        """
        Dynamic initializer for ItemRenderer.
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
    def registerBlockModel(self, arg0: 'BlockItem', arg1: 'Supplier'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.registerBlockModel(dev.ultreon.quantum.item.BlockItem,java.util.function.Supplier<dev.ultreon.quantum.client.model.block.BlockModel>)"""
        super(__ItemRenderer, self).registerBlockModel(arg0, arg1)

    @overload
    def reload(self):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.reload()"""
        super(ItemRenderer, self).reload()

    @overload
    def registerModel(self, arg0: 'Item', arg1: 'ItemModel'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.registerModel(dev.ultreon.quantum.item.Item,dev.ultreon.quantum.client.model.item.ItemModel)"""
        super(__ItemRenderer, self).registerModel(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def render(self, arg0: 'Item', arg1: 'Renderer', arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.render(dev.ultreon.quantum.item.Item,dev.ultreon.quantum.client.gui.Renderer,int,int)"""
        super(__ItemRenderer, self).render(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getItemCam(self) -> 'graphics.OrthographicCamera':
        """public com.badlogic.gdx.graphics.OrthographicCamera dev.ultreon.quantum.client.item.ItemRenderer.getItemCam()"""
        return 'graphics.OrthographicCamera'.__wrap(super(ItemRenderer, self).getItemCam())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.dispose()"""
        super(ItemRenderer, self).dispose()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def registerModels(self, arg0: 'Json5ModelLoader'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.registerModels(dev.ultreon.quantum.client.model.model.Json5ModelLoader)"""
        super(__ItemRenderer, self).registerModels(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def loadModels(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.loadModels(dev.ultreon.quantum.client.QuantumClient)"""
        super(__ItemRenderer, self).loadModels(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def createModelInstance(self, arg0: 'ItemStack') -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.item.ItemRenderer.createModelInstance(dev.ultreon.quantum.item.ItemStack)"""
        return 'g3d.ModelInstance'.__wrap(super(__ItemRenderer, self).createModelInstance(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.resize(int,int)"""
        super(__ItemRenderer, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.item.ItemRenderer(dev.ultreon.quantum.client.QuantumClient)"""
        val = __ItemRenderer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.client.item.ItemRenderer