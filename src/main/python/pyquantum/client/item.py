from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
from builtins import str
import com.badlogic.gdx.graphics.g3d.ModelInstance as _ModelInstance
_ModelInstance = _ModelInstance
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum.client.model import item
except ImportError:
    item = _import_once("pyquantum.client.model.item")

import com.badlogic.gdx.graphics.OrthographicCamera as _OrthographicCamera
_OrthographicCamera = _OrthographicCamera
import java.lang.Integer as _int
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

try:
    from pyquantum.client.model import model
except ImportError:
    model = _import_once("pyquantum.client.model.model")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import dev.ultreon.quantum.client.item.ItemRenderer as _ItemRenderer
_ItemRenderer = _ItemRenderer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ItemRenderer():
    """dev.ultreon.quantum.client.item.ItemRenderer"""
 
    @staticmethod
    def _wrap(java_value: _ItemRenderer) -> 'ItemRenderer':
        return ItemRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemRenderer):
        """
        Dynamic initializer for ItemRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def loadModels(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.loadModels(dev.ultreon.quantum.client.QuantumClient)"""
        super(_ItemRenderer, self).loadModels(arg0)

    @overload
    def reload(self):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.reload()"""
        super(ItemRenderer, self).reload()

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.item.ItemRenderer(dev.ultreon.quantum.client.QuantumClient)"""
        val = _ItemRenderer(arg0)
        self.__wrapper = val

    @overload
    def registerModel(self, arg0: 'Item', arg1: 'ItemModel'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.registerModel(dev.ultreon.quantum.item.Item,dev.ultreon.quantum.client.model.item.ItemModel)"""
        super(_ItemRenderer, self).registerModel(arg0, arg1)

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
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.resize(int,int)"""
        super(_ItemRenderer, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.dispose()"""
        super(ItemRenderer, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def createModelInstance(self, arg0: 'ItemStack') -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.item.ItemRenderer.createModelInstance(dev.ultreon.quantum.item.ItemStack)"""
        return 'g3d.ModelInstance'._wrap(super(_ItemRenderer, self).createModelInstance(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def render(self, arg0: 'Item', arg1: 'Renderer', arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.render(dev.ultreon.quantum.item.Item,dev.ultreon.quantum.client.gui.Renderer,int,int)"""
        super(_ItemRenderer, self).render(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def registerModels(self, arg0: 'Json5ModelLoader'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.registerModels(dev.ultreon.quantum.client.model.model.Json5ModelLoader)"""
        super(_ItemRenderer, self).registerModels(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def registerBlockModel(self, arg0: 'BlockItem', arg1: 'Supplier'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.registerBlockModel(dev.ultreon.quantum.item.BlockItem,java.util.function.Supplier<dev.ultreon.quantum.client.model.block.BlockModel>)"""
        super(_ItemRenderer, self).registerBlockModel(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getItemCam(self) -> 'graphics.OrthographicCamera':
        """public com.badlogic.gdx.graphics.OrthographicCamera dev.ultreon.quantum.client.item.ItemRenderer.getItemCam()"""
        return 'graphics.OrthographicCamera'._wrap(super(ItemRenderer, self).getItemCam())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.item.ItemRenderer
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
from builtins import str
import com.badlogic.gdx.graphics.g3d.ModelInstance as _ModelInstance
_ModelInstance = _ModelInstance
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum.client.model import item
except ImportError:
    item = _import_once("pyquantum.client.model.item")

import com.badlogic.gdx.graphics.OrthographicCamera as _OrthographicCamera
_OrthographicCamera = _OrthographicCamera
import java.lang.Integer as _int
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

try:
    from pyquantum.client.model import model
except ImportError:
    model = _import_once("pyquantum.client.model.model")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import dev.ultreon.quantum.client.item.ItemRenderer as _ItemRenderer
_ItemRenderer = _ItemRenderer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ItemRenderer():
    """dev.ultreon.quantum.client.item.ItemRenderer"""
 
    @staticmethod
    def _wrap(java_value: _ItemRenderer) -> 'ItemRenderer':
        return ItemRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemRenderer):
        """
        Dynamic initializer for ItemRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def loadModels(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.loadModels(dev.ultreon.quantum.client.QuantumClient)"""
        super(_ItemRenderer, self).loadModels(arg0)

    @overload
    def reload(self):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.reload()"""
        super(ItemRenderer, self).reload()

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.item.ItemRenderer(dev.ultreon.quantum.client.QuantumClient)"""
        val = _ItemRenderer(arg0)
        self.__wrapper = val

    @overload
    def registerModel(self, arg0: 'Item', arg1: 'ItemModel'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.registerModel(dev.ultreon.quantum.item.Item,dev.ultreon.quantum.client.model.item.ItemModel)"""
        super(_ItemRenderer, self).registerModel(arg0, arg1)

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
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.resize(int,int)"""
        super(_ItemRenderer, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.dispose()"""
        super(ItemRenderer, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def createModelInstance(self, arg0: 'ItemStack') -> 'g3d.ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance dev.ultreon.quantum.client.item.ItemRenderer.createModelInstance(dev.ultreon.quantum.item.ItemStack)"""
        return 'g3d.ModelInstance'._wrap(super(_ItemRenderer, self).createModelInstance(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def render(self, arg0: 'Item', arg1: 'Renderer', arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.render(dev.ultreon.quantum.item.Item,dev.ultreon.quantum.client.gui.Renderer,int,int)"""
        super(_ItemRenderer, self).render(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def registerModels(self, arg0: 'Json5ModelLoader'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.registerModels(dev.ultreon.quantum.client.model.model.Json5ModelLoader)"""
        super(_ItemRenderer, self).registerModels(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def registerBlockModel(self, arg0: 'BlockItem', arg1: 'Supplier'):
        """public void dev.ultreon.quantum.client.item.ItemRenderer.registerBlockModel(dev.ultreon.quantum.item.BlockItem,java.util.function.Supplier<dev.ultreon.quantum.client.model.block.BlockModel>)"""
        super(_ItemRenderer, self).registerBlockModel(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getItemCam(self) -> 'graphics.OrthographicCamera':
        """public com.badlogic.gdx.graphics.OrthographicCamera dev.ultreon.quantum.client.item.ItemRenderer.getItemCam()"""
        return 'graphics.OrthographicCamera'._wrap(super(ItemRenderer, self).getItemCam())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.item.ItemRenderer