from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer as _PlayerRenderer
_PlayerRenderer = _PlayerRenderer
try:
    from pyquantum.client import model
except ImportError:
    model = _import_once("pyquantum.client.model")

try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as _EntityRenderer
_EntityRenderer = _EntityRenderer
import java.lang.Float as _float
try:
    from pyquantum.client.model import entity
except ImportError:
    entity = _import_once("pyquantum.client.model.entity")

import dev.ultreon.quantum.client.model.entity.EntityModel as _EntityModel
_EntityModel = _EntityModel
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer as _LivingEntityRenderer
_LivingEntityRenderer = _LivingEntityRenderer
import dev.ultreon.quantum.client.render.EntityTextures as _EntityTextures
_EntityTextures = _EntityTextures
import dev.ultreon.quantum.client.model.QVModel as _QVModel
_QVModel = _QVModel
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlayerRenderer():
    """dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer"""
 
    @staticmethod
    def _wrap(java_value: _PlayerRenderer) -> 'PlayerRenderer':
        return PlayerRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerRenderer):
        """
        Dynamic initializer for PlayerRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<dev.ultreon.quantum.entity.player.Player>,dev.ultreon.quantum.client.model.WorldRenderContext<dev.ultreon.quantum.entity.player.Player>)"""
        super(_PlayerRenderer, self).animate(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

    @override
    @overload
    def getEntityModel(self) -> 'entity.EntityModel':
        """public dev.ultreon.quantum.client.model.entity.EntityModel<E> dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.getEntityModel()"""
        return 'entity.EntityModel'._wrap(super(LivingEntityRenderer, self).getEntityModel())

    @overload
    def createModel(self, arg0: 'LivingEntity') -> 'model.QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.createModel(E)"""
        return 'model.QVModel'._wrap(super(_LivingEntityRenderer, self).createModel(arg0))

    @staticmethod
    @overload
    def updateWalkAnim(arg0: 'LivingEntity', arg1: float, arg2: float, arg3: float):
        """public static void dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.updateWalkAnim(dev.ultreon.quantum.entity.LivingEntity,float,float,float)"""
        _LivingEntityRenderer.updateWalkAnim(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

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
    def __init__(self, arg0: 'PlayerModel', arg1: 'Model'):
        """public dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer(dev.ultreon.quantum.client.model.entity.PlayerModel<dev.ultreon.quantum.entity.player.Player>,com.badlogic.gdx.graphics.g3d.Model)"""
        val = _PlayerRenderer(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(_EntityRenderer, self).render(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getTextures(self) -> 'render.EntityTextures':
        """public dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer.getTextures()"""
        return 'render.EntityTextures'._wrap(super(PlayerRenderer, self).getTextures())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer as _PlayerRenderer
_PlayerRenderer = _PlayerRenderer
try:
    from pyquantum.client import model
except ImportError:
    model = _import_once("pyquantum.client.model")

try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as _EntityRenderer
_EntityRenderer = _EntityRenderer
import java.lang.Float as _float
try:
    from pyquantum.client.model import entity
except ImportError:
    entity = _import_once("pyquantum.client.model.entity")

import dev.ultreon.quantum.client.model.entity.EntityModel as _EntityModel
_EntityModel = _EntityModel
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer as _LivingEntityRenderer
_LivingEntityRenderer = _LivingEntityRenderer
import dev.ultreon.quantum.client.render.EntityTextures as _EntityTextures
_EntityTextures = _EntityTextures
import dev.ultreon.quantum.client.model.QVModel as _QVModel
_QVModel = _QVModel
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlayerRenderer():
    """dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer"""
 
    @staticmethod
    def _wrap(java_value: _PlayerRenderer) -> 'PlayerRenderer':
        return PlayerRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerRenderer):
        """
        Dynamic initializer for PlayerRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<dev.ultreon.quantum.entity.player.Player>,dev.ultreon.quantum.client.model.WorldRenderContext<dev.ultreon.quantum.entity.player.Player>)"""
        super(_PlayerRenderer, self).animate(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

    @override
    @overload
    def getEntityModel(self) -> 'entity.EntityModel':
        """public dev.ultreon.quantum.client.model.entity.EntityModel<E> dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.getEntityModel()"""
        return 'entity.EntityModel'._wrap(super(LivingEntityRenderer, self).getEntityModel())

    @overload
    def createModel(self, arg0: 'LivingEntity') -> 'model.QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.createModel(E)"""
        return 'model.QVModel'._wrap(super(_LivingEntityRenderer, self).createModel(arg0))

    @staticmethod
    @overload
    def updateWalkAnim(arg0: 'LivingEntity', arg1: float, arg2: float, arg3: float):
        """public static void dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.updateWalkAnim(dev.ultreon.quantum.entity.LivingEntity,float,float,float)"""
        _LivingEntityRenderer.updateWalkAnim(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

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
    def __init__(self, arg0: 'PlayerModel', arg1: 'Model'):
        """public dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer(dev.ultreon.quantum.client.model.entity.PlayerModel<dev.ultreon.quantum.entity.player.Player>,com.badlogic.gdx.graphics.g3d.Model)"""
        val = _PlayerRenderer(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(_EntityRenderer, self).render(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getTextures(self) -> 'render.EntityTextures':
        """public dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer.getTextures()"""
        return 'render.EntityTextures'._wrap(super(PlayerRenderer, self).getTextures())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer 
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer as _DroppedItemRenderer
_DroppedItemRenderer = _DroppedItemRenderer
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

try:
    from pyquantum.client import model
except ImportError:
    model = _import_once("pyquantum.client.model")

try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as _EntityRenderer
_EntityRenderer = _EntityRenderer
try:
    from pyquantum.client.model import entity
except ImportError:
    entity = _import_once("pyquantum.client.model.entity")

import java.lang.Integer as _int
import dev.ultreon.quantum.client.render.EntityTextures as _EntityTextures
_EntityTextures = _EntityTextures
import dev.ultreon.quantum.client.model.QVModel as _QVModel
_QVModel = _QVModel
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DroppedItemRenderer():
    """dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer"""
 
    @staticmethod
    def _wrap(java_value: _DroppedItemRenderer) -> 'DroppedItemRenderer':
        return DroppedItemRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DroppedItemRenderer):
        """
        Dynamic initializer for DroppedItemRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DroppedItemRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DroppedItemRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

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
    def createModel(self, arg0: 'DroppedItem') -> 'model.QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer.createModel(dev.ultreon.quantum.entity.DroppedItem)"""
        return 'model.QVModel'._wrap(super(_DroppedItemRenderer, self).createModel(arg0))

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
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<dev.ultreon.quantum.entity.DroppedItem>,dev.ultreon.quantum.client.model.WorldRenderContext<dev.ultreon.quantum.entity.DroppedItem>)"""
        super(_DroppedItemRenderer, self).animate(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTextures(self) -> 'render.EntityTextures':
        """public dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer.getTextures()"""
        return 'render.EntityTextures'._wrap(super(DroppedItemRenderer, self).getTextures())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(_EntityRenderer, self).render(arg0, arg1)

    @overload
    def __init__(self, arg0: 'EntityModel', arg1: 'Model'):
        """public dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer(dev.ultreon.quantum.client.model.entity.EntityModel<dev.ultreon.quantum.entity.DroppedItem>,com.badlogic.gdx.graphics.g3d.Model)"""
        val = _DroppedItemRenderer(arg0, arg1)
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
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.SomethingRenderer
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.model.entity.renderer.SomethingRenderer as _SomethingRenderer
_SomethingRenderer = _SomethingRenderer
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

try:
    from pyquantum.client import model
except ImportError:
    model = _import_once("pyquantum.client.model")

try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as _EntityRenderer
_EntityRenderer = _EntityRenderer
import java.lang.Float as _float
try:
    from pyquantum.client.model import entity
except ImportError:
    entity = _import_once("pyquantum.client.model.entity")

import dev.ultreon.quantum.client.model.entity.EntityModel as _EntityModel
_EntityModel = _EntityModel
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer as _LivingEntityRenderer
_LivingEntityRenderer = _LivingEntityRenderer
import dev.ultreon.quantum.client.render.EntityTextures as _EntityTextures
_EntityTextures = _EntityTextures
import dev.ultreon.quantum.client.model.QVModel as _QVModel
_QVModel = _QVModel
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SomethingRenderer():
    """dev.ultreon.quantum.client.model.entity.renderer.SomethingRenderer"""
 
    @staticmethod
    def _wrap(java_value: _SomethingRenderer) -> 'SomethingRenderer':
        return SomethingRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SomethingRenderer):
        """
        Dynamic initializer for SomethingRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SomethingRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SomethingRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

    @override
    @overload
    def getEntityModel(self) -> 'entity.EntityModel':
        """public dev.ultreon.quantum.client.model.entity.EntityModel<E> dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.getEntityModel()"""
        return 'entity.EntityModel'._wrap(super(LivingEntityRenderer, self).getEntityModel())

    @overload
    def createModel(self, arg0: 'LivingEntity') -> 'model.QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.createModel(E)"""
        return 'model.QVModel'._wrap(super(_LivingEntityRenderer, self).createModel(arg0))

    @staticmethod
    @overload
    def updateWalkAnim(arg0: 'LivingEntity', arg1: float, arg2: float, arg3: float):
        """public static void dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.updateWalkAnim(dev.ultreon.quantum.entity.LivingEntity,float,float,float)"""
        _LivingEntityRenderer.updateWalkAnim(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.SomethingRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<dev.ultreon.quantum.entity.Something>,dev.ultreon.quantum.client.model.WorldRenderContext<dev.ultreon.quantum.entity.Something>)"""
        super(_SomethingRenderer, self).animate(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getTextures(self) -> 'render.EntityTextures':
        """public dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.SomethingRenderer.getTextures()"""
        return 'render.EntityTextures'._wrap(super(SomethingRenderer, self).getTextures())

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

    @override
    @overload
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(_EntityRenderer, self).render(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'EntityModel', arg1: 'Model'):
        """public dev.ultreon.quantum.client.model.entity.renderer.SomethingRenderer(dev.ultreon.quantum.client.model.entity.EntityModel<dev.ultreon.quantum.entity.Something>,com.badlogic.gdx.graphics.g3d.Model)"""
        val = _SomethingRenderer(arg0, arg1)
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
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client import model
except ImportError:
    model = _import_once("pyquantum.client.model")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as _EntityRenderer
_EntityRenderer = _EntityRenderer
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntityRenderer():
    """dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer"""
 
    @staticmethod
    def _wrap(java_value: _EntityRenderer) -> 'EntityRenderer':
        return EntityRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityRenderer):
        """
        Dynamic initializer for EntityRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(_EntityRenderer, self).render(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

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

    @abstractmethod
    def createModel(self, arg0: 'Entity'):
        """public abstract dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.createModel(E)"""
        pass

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

    @abstractmethod
    def getTextures(self, ):
        """public abstract dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.getTextures()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public abstract void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.PigRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

try:
    from pyquantum.client import model
except ImportError:
    model = _import_once("pyquantum.client.model")

try:
    from pyquantum.client import render
except ImportError:
    render = _import_once("pyquantum.client.render")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as _EntityRenderer
_EntityRenderer = _EntityRenderer
import java.lang.Float as _float
import dev.ultreon.quantum.client.model.entity.renderer.PigRenderer as _PigRenderer
_PigRenderer = _PigRenderer
try:
    from pyquantum.client.model import entity
except ImportError:
    entity = _import_once("pyquantum.client.model.entity")

import dev.ultreon.quantum.client.model.entity.EntityModel as _EntityModel
_EntityModel = _EntityModel
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer as _LivingEntityRenderer
_LivingEntityRenderer = _LivingEntityRenderer
import dev.ultreon.quantum.client.render.EntityTextures as _EntityTextures
_EntityTextures = _EntityTextures
import dev.ultreon.quantum.client.model.QVModel as _QVModel
_QVModel = _QVModel
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PigRenderer():
    """dev.ultreon.quantum.client.model.entity.renderer.PigRenderer"""
 
    @staticmethod
    def _wrap(java_value: _PigRenderer) -> 'PigRenderer':
        return PigRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PigRenderer):
        """
        Dynamic initializer for PigRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PigRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PigRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

    @override
    @overload
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.PigRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<dev.ultreon.quantum.entity.Pig>,dev.ultreon.quantum.client.model.WorldRenderContext<dev.ultreon.quantum.entity.Pig>)"""
        super(_PigRenderer, self).animate(arg0, arg1)

    @override
    @overload
    def getEntityModel(self) -> 'entity.EntityModel':
        """public dev.ultreon.quantum.client.model.entity.EntityModel<E> dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.getEntityModel()"""
        return 'entity.EntityModel'._wrap(super(LivingEntityRenderer, self).getEntityModel())

    @overload
    def createModel(self, arg0: 'LivingEntity') -> 'model.QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.createModel(E)"""
        return 'model.QVModel'._wrap(super(_LivingEntityRenderer, self).createModel(arg0))

    @staticmethod
    @overload
    def updateWalkAnim(arg0: 'LivingEntity', arg1: float, arg2: float, arg3: float):
        """public static void dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.updateWalkAnim(dev.ultreon.quantum.entity.LivingEntity,float,float,float)"""
        _LivingEntityRenderer.updateWalkAnim(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

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
    def getTextures(self) -> 'render.EntityTextures':
        """public dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.PigRenderer.getTextures()"""
        return 'render.EntityTextures'._wrap(super(PigRenderer, self).getTextures())

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
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(_EntityRenderer, self).render(arg0, arg1)

    @overload
    def __init__(self, arg0: 'EntityModel', arg1: 'Model'):
        """public dev.ultreon.quantum.client.model.entity.renderer.PigRenderer(dev.ultreon.quantum.client.model.entity.EntityModel<dev.ultreon.quantum.entity.Pig>,com.badlogic.gdx.graphics.g3d.Model)"""
        val = _PigRenderer(arg0, arg1)
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
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client import model
except ImportError:
    model = _import_once("pyquantum.client.model")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as _EntityRenderer
_EntityRenderer = _EntityRenderer
import java.lang.Float as _float
try:
    from pyquantum.client.model import entity
except ImportError:
    entity = _import_once("pyquantum.client.model.entity")

import dev.ultreon.quantum.client.model.entity.EntityModel as _EntityModel
_EntityModel = _EntityModel
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer as _LivingEntityRenderer
_LivingEntityRenderer = _LivingEntityRenderer
import dev.ultreon.quantum.client.model.QVModel as _QVModel
_QVModel = _QVModel
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LivingEntityRenderer():
    """dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer"""
 
    @staticmethod
    def _wrap(java_value: _LivingEntityRenderer) -> 'LivingEntityRenderer':
        return LivingEntityRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LivingEntityRenderer):
        """
        Dynamic initializer for LivingEntityRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LivingEntityRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LivingEntityRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

    @overload
    def createModel(self, arg0: 'LivingEntity') -> 'model.QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.createModel(E)"""
        return 'model.QVModel'._wrap(super(_LivingEntityRenderer, self).createModel(arg0))

    @staticmethod
    @overload
    def updateWalkAnim(arg0: 'LivingEntity', arg1: float, arg2: float, arg3: float):
        """public static void dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.updateWalkAnim(dev.ultreon.quantum.entity.LivingEntity,float,float,float)"""
        _LivingEntityRenderer.updateWalkAnim(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

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

    @overload
    def getEntityModel(self) -> 'entity.EntityModel':
        """public dev.ultreon.quantum.client.model.entity.EntityModel<E> dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.getEntityModel()"""
        return 'entity.EntityModel'._wrap(super(LivingEntityRenderer, self).getEntityModel())

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
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(_EntityRenderer, self).render(arg0, arg1)

    @abstractmethod
    def getTextures(self, ):
        """public abstract dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.getTextures()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public abstract void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())