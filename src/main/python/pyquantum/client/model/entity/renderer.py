from __future__ import annotations
from overload import overload


 
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
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer as __LivingEntityRenderer
__LivingEntityRenderer = __LivingEntityRenderer
try:
    from pyquantum.client import model
except ImportError:
    model = __import_once__("pyquantum.client.model")

import dev.ultreon.quantum.client.model.QVModel as __QVModel
__QVModel = __QVModel
try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

import dev.ultreon.quantum.client.model.entity.EntityModel as __EntityModel
__EntityModel = __EntityModel
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as __EntityRenderer
__EntityRenderer = __EntityRenderer
import dev.ultreon.quantum.client.render.EntityTextures as __EntityTextures
__EntityTextures = __EntityTextures
try:
    from pyquantum.client.model import entity
except ImportError:
    entity = __import_once__("pyquantum.client.model.entity")

import java.lang.Long as __long
import dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer as __PlayerRenderer
__PlayerRenderer = __PlayerRenderer
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PlayerRenderer(__LivingEntityRenderer, LivingEntityRenderer):
    """dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer"""
 
    @staticmethod
    def __wrap(java_value: __PlayerRenderer) -> 'PlayerRenderer':
        return PlayerRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayerRenderer):
        """
        Dynamic initializer for PlayerRenderer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

    @override
    @overload
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(__EntityRenderer, self).render(arg0, arg1)

    @override
    @overload
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<dev.ultreon.quantum.entity.player.Player>,dev.ultreon.quantum.client.model.WorldRenderContext<dev.ultreon.quantum.entity.player.Player>)"""
        super(__PlayerRenderer, self).animate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def createModel(self, arg0: 'LivingEntity') -> 'model.QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.createModel(E)"""
        return 'model.QVModel'.__wrap(super(__LivingEntityRenderer, self).createModel(arg0))

    @override
    @overload
    def getEntityModel(self) -> 'entity.EntityModel':
        """public dev.ultreon.quantum.client.model.entity.EntityModel<E> dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.getEntityModel()"""
        return 'entity.EntityModel'.__wrap(super(LivingEntityRenderer, self).getEntityModel())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def updateWalkAnim(arg0: 'LivingEntity', arg1: float, arg2: float, arg3: float):
        """public static void dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.updateWalkAnim(dev.ultreon.quantum.entity.LivingEntity,float,float,float)"""
        __LivingEntityRenderer.updateWalkAnim(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

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
    def getTextures(self) -> 'render.EntityTextures':
        """public dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer.getTextures()"""
        return 'render.EntityTextures'.__wrap(super(PlayerRenderer, self).getTextures())

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

    @overload
    def __init__(self, arg0: 'PlayerModel', arg1: 'Model'):
        """public dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer(dev.ultreon.quantum.client.model.entity.PlayerModel<dev.ultreon.quantum.entity.player.Player>,com.badlogic.gdx.graphics.g3d.Model)"""
        val = __PlayerRenderer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer
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
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer as __LivingEntityRenderer
__LivingEntityRenderer = __LivingEntityRenderer
try:
    from pyquantum.client import model
except ImportError:
    model = __import_once__("pyquantum.client.model")

import dev.ultreon.quantum.client.model.QVModel as __QVModel
__QVModel = __QVModel
try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

import dev.ultreon.quantum.client.model.entity.EntityModel as __EntityModel
__EntityModel = __EntityModel
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as __EntityRenderer
__EntityRenderer = __EntityRenderer
import dev.ultreon.quantum.client.render.EntityTextures as __EntityTextures
__EntityTextures = __EntityTextures
try:
    from pyquantum.client.model import entity
except ImportError:
    entity = __import_once__("pyquantum.client.model.entity")

import java.lang.Long as __long
import dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer as __PlayerRenderer
__PlayerRenderer = __PlayerRenderer
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PlayerRenderer(__LivingEntityRenderer, LivingEntityRenderer):
    """dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer"""
 
    @staticmethod
    def __wrap(java_value: __PlayerRenderer) -> 'PlayerRenderer':
        return PlayerRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayerRenderer):
        """
        Dynamic initializer for PlayerRenderer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

    @override
    @overload
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(__EntityRenderer, self).render(arg0, arg1)

    @override
    @overload
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<dev.ultreon.quantum.entity.player.Player>,dev.ultreon.quantum.client.model.WorldRenderContext<dev.ultreon.quantum.entity.player.Player>)"""
        super(__PlayerRenderer, self).animate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def createModel(self, arg0: 'LivingEntity') -> 'model.QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.createModel(E)"""
        return 'model.QVModel'.__wrap(super(__LivingEntityRenderer, self).createModel(arg0))

    @override
    @overload
    def getEntityModel(self) -> 'entity.EntityModel':
        """public dev.ultreon.quantum.client.model.entity.EntityModel<E> dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.getEntityModel()"""
        return 'entity.EntityModel'.__wrap(super(LivingEntityRenderer, self).getEntityModel())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def updateWalkAnim(arg0: 'LivingEntity', arg1: float, arg2: float, arg3: float):
        """public static void dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.updateWalkAnim(dev.ultreon.quantum.entity.LivingEntity,float,float,float)"""
        __LivingEntityRenderer.updateWalkAnim(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

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
    def getTextures(self) -> 'render.EntityTextures':
        """public dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer.getTextures()"""
        return 'render.EntityTextures'.__wrap(super(PlayerRenderer, self).getTextures())

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

    @overload
    def __init__(self, arg0: 'PlayerModel', arg1: 'Model'):
        """public dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer(dev.ultreon.quantum.client.model.entity.PlayerModel<dev.ultreon.quantum.entity.player.Player>,com.badlogic.gdx.graphics.g3d.Model)"""
        val = __PlayerRenderer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.PlayerRenderer 
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer
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
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

try:
    from pyquantum.client import model
except ImportError:
    model = __import_once__("pyquantum.client.model")

import dev.ultreon.quantum.client.model.QVModel as __QVModel
__QVModel = __QVModel
try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as __EntityRenderer
__EntityRenderer = __EntityRenderer
import dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer as __DroppedItemRenderer
__DroppedItemRenderer = __DroppedItemRenderer
import dev.ultreon.quantum.client.render.EntityTextures as __EntityTextures
__EntityTextures = __EntityTextures
import java.lang.Long as __long
try:
    from pyquantum.client.model import entity
except ImportError:
    entity = __import_once__("pyquantum.client.model.entity")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DroppedItemRenderer(__EntityRenderer, EntityRenderer):
    """dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer"""
 
    @staticmethod
    def __wrap(java_value: __DroppedItemRenderer) -> 'DroppedItemRenderer':
        return DroppedItemRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DroppedItemRenderer):
        """
        Dynamic initializer for DroppedItemRenderer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

    @override
    @overload
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(__EntityRenderer, self).render(arg0, arg1)

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
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<dev.ultreon.quantum.entity.DroppedItem>,dev.ultreon.quantum.client.model.WorldRenderContext<dev.ultreon.quantum.entity.DroppedItem>)"""
        super(__DroppedItemRenderer, self).animate(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def createModel(self, arg0: 'DroppedItem') -> 'model.QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer.createModel(dev.ultreon.quantum.entity.DroppedItem)"""
        return 'model.QVModel'.__wrap(super(__DroppedItemRenderer, self).createModel(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getTextures(self) -> 'render.EntityTextures':
        """public dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer.getTextures()"""
        return 'render.EntityTextures'.__wrap(super(DroppedItemRenderer, self).getTextures())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'EntityModel', arg1: 'Model'):
        """public dev.ultreon.quantum.client.model.entity.renderer.DroppedItemRenderer(dev.ultreon.quantum.client.model.entity.EntityModel<dev.ultreon.quantum.entity.DroppedItem>,com.badlogic.gdx.graphics.g3d.Model)"""
        val = __DroppedItemRenderer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.SomethingRenderer
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.model.entity.renderer.SomethingRenderer as __SomethingRenderer
__SomethingRenderer = __SomethingRenderer
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import java.lang.Object as __object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer as __LivingEntityRenderer
__LivingEntityRenderer = __LivingEntityRenderer
try:
    from pyquantum.client import model
except ImportError:
    model = __import_once__("pyquantum.client.model")

import dev.ultreon.quantum.client.model.QVModel as __QVModel
__QVModel = __QVModel
try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

import dev.ultreon.quantum.client.model.entity.EntityModel as __EntityModel
__EntityModel = __EntityModel
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as __EntityRenderer
__EntityRenderer = __EntityRenderer
import dev.ultreon.quantum.client.render.EntityTextures as __EntityTextures
__EntityTextures = __EntityTextures
try:
    from pyquantum.client.model import entity
except ImportError:
    entity = __import_once__("pyquantum.client.model.entity")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SomethingRenderer(__LivingEntityRenderer, LivingEntityRenderer):
    """dev.ultreon.quantum.client.model.entity.renderer.SomethingRenderer"""
 
    @staticmethod
    def __wrap(java_value: __SomethingRenderer) -> 'SomethingRenderer':
        return SomethingRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SomethingRenderer):
        """
        Dynamic initializer for SomethingRenderer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

    @override
    @overload
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(__EntityRenderer, self).render(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def createModel(self, arg0: 'LivingEntity') -> 'model.QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.createModel(E)"""
        return 'model.QVModel'.__wrap(super(__LivingEntityRenderer, self).createModel(arg0))

    @override
    @overload
    def getEntityModel(self) -> 'entity.EntityModel':
        """public dev.ultreon.quantum.client.model.entity.EntityModel<E> dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.getEntityModel()"""
        return 'entity.EntityModel'.__wrap(super(LivingEntityRenderer, self).getEntityModel())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def updateWalkAnim(arg0: 'LivingEntity', arg1: float, arg2: float, arg3: float):
        """public static void dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.updateWalkAnim(dev.ultreon.quantum.entity.LivingEntity,float,float,float)"""
        __LivingEntityRenderer.updateWalkAnim(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

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
    def getTextures(self) -> 'render.EntityTextures':
        """public dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.SomethingRenderer.getTextures()"""
        return 'render.EntityTextures'.__wrap(super(SomethingRenderer, self).getTextures())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'EntityModel', arg1: 'Model'):
        """public dev.ultreon.quantum.client.model.entity.renderer.SomethingRenderer(dev.ultreon.quantum.client.model.entity.EntityModel<dev.ultreon.quantum.entity.Something>,com.badlogic.gdx.graphics.g3d.Model)"""
        val = __SomethingRenderer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.SomethingRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<dev.ultreon.quantum.entity.Something>,dev.ultreon.quantum.client.model.WorldRenderContext<dev.ultreon.quantum.entity.Something>)"""
        super(__SomethingRenderer, self).animate(arg0, arg1)

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
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer
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
    from pyquantum.client import model
except ImportError:
    model = __import_once__("pyquantum.client.model")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as __EntityRenderer
__EntityRenderer = __EntityRenderer
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
 
class EntityRenderer(ABC, pygdx.__Disposable, utils.Disposable):
    """dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer"""
 
    @staticmethod
    def __wrap(java_value: __EntityRenderer) -> 'EntityRenderer':
        return EntityRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityRenderer):
        """
        Dynamic initializer for EntityRenderer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(__EntityRenderer, self).render(arg0, arg1)

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @abstractmethod
    def getTextures(self, ):
        """public abstract dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.getTextures()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public abstract void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.PigRenderer
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.model.entity.renderer.PigRenderer as __PigRenderer
__PigRenderer = __PigRenderer
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import java.lang.Object as __object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer as __LivingEntityRenderer
__LivingEntityRenderer = __LivingEntityRenderer
try:
    from pyquantum.client import model
except ImportError:
    model = __import_once__("pyquantum.client.model")

import dev.ultreon.quantum.client.model.QVModel as __QVModel
__QVModel = __QVModel
try:
    from pyquantum.client import render
except ImportError:
    render = __import_once__("pyquantum.client.render")

import dev.ultreon.quantum.client.model.entity.EntityModel as __EntityModel
__EntityModel = __EntityModel
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as __EntityRenderer
__EntityRenderer = __EntityRenderer
import dev.ultreon.quantum.client.render.EntityTextures as __EntityTextures
__EntityTextures = __EntityTextures
try:
    from pyquantum.client.model import entity
except ImportError:
    entity = __import_once__("pyquantum.client.model.entity")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PigRenderer(__LivingEntityRenderer, LivingEntityRenderer):
    """dev.ultreon.quantum.client.model.entity.renderer.PigRenderer"""
 
    @staticmethod
    def __wrap(java_value: __PigRenderer) -> 'PigRenderer':
        return PigRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PigRenderer):
        """
        Dynamic initializer for PigRenderer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

    @override
    @overload
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(__EntityRenderer, self).render(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def createModel(self, arg0: 'LivingEntity') -> 'model.QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.createModel(E)"""
        return 'model.QVModel'.__wrap(super(__LivingEntityRenderer, self).createModel(arg0))

    @override
    @overload
    def getEntityModel(self) -> 'entity.EntityModel':
        """public dev.ultreon.quantum.client.model.entity.EntityModel<E> dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.getEntityModel()"""
        return 'entity.EntityModel'.__wrap(super(LivingEntityRenderer, self).getEntityModel())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.PigRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<dev.ultreon.quantum.entity.Pig>,dev.ultreon.quantum.client.model.WorldRenderContext<dev.ultreon.quantum.entity.Pig>)"""
        super(__PigRenderer, self).animate(arg0, arg1)

    @staticmethod
    @overload
    def updateWalkAnim(arg0: 'LivingEntity', arg1: float, arg2: float, arg3: float):
        """public static void dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.updateWalkAnim(dev.ultreon.quantum.entity.LivingEntity,float,float,float)"""
        __LivingEntityRenderer.updateWalkAnim(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

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

    @overload
    def __init__(self, arg0: 'EntityModel', arg1: 'Model'):
        """public dev.ultreon.quantum.client.model.entity.renderer.PigRenderer(dev.ultreon.quantum.client.model.entity.EntityModel<dev.ultreon.quantum.entity.Pig>,com.badlogic.gdx.graphics.g3d.Model)"""
        val = __PigRenderer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTextures(self) -> 'render.EntityTextures':
        """public dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.PigRenderer.getTextures()"""
        return 'render.EntityTextures'.__wrap(super(PigRenderer, self).getTextures())

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
 
 
# CLASS: dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer as __LivingEntityRenderer
__LivingEntityRenderer = __LivingEntityRenderer
try:
    from pyquantum.client import model
except ImportError:
    model = __import_once__("pyquantum.client.model")

import dev.ultreon.quantum.client.model.QVModel as __QVModel
__QVModel = __QVModel
import dev.ultreon.quantum.client.model.entity.EntityModel as __EntityModel
__EntityModel = __EntityModel
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer as __EntityRenderer
__EntityRenderer = __EntityRenderer
try:
    from pyquantum.client.model import entity
except ImportError:
    entity = __import_once__("pyquantum.client.model.entity")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LivingEntityRenderer(ABC, __EntityRenderer, EntityRenderer):
    """dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer"""
 
    @staticmethod
    def __wrap(java_value: __LivingEntityRenderer) -> 'LivingEntityRenderer':
        return LivingEntityRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LivingEntityRenderer):
        """
        Dynamic initializer for LivingEntityRenderer.
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
    def dispose(self):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.dispose()"""
        super(EntityRenderer, self).dispose()

    @override
    @overload
    def render(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.render(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        super(__EntityRenderer, self).render(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def createModel(self, arg0: 'LivingEntity') -> 'model.QVModel':
        """public dev.ultreon.quantum.client.model.QVModel dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.createModel(E)"""
        return 'model.QVModel'.__wrap(super(__LivingEntityRenderer, self).createModel(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getEntityModel(self) -> 'entity.EntityModel':
        """public dev.ultreon.quantum.client.model.entity.EntityModel<E> dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.getEntityModel()"""
        return 'entity.EntityModel'.__wrap(super(LivingEntityRenderer, self).getEntityModel())

    @staticmethod
    @overload
    def updateWalkAnim(arg0: 'LivingEntity', arg1: float, arg2: float, arg3: float):
        """public static void dev.ultreon.quantum.client.model.entity.renderer.LivingEntityRenderer.updateWalkAnim(dev.ultreon.quantum.entity.LivingEntity,float,float,float)"""
        __LivingEntityRenderer.updateWalkAnim(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

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

    @abstractmethod
    def getTextures(self, ):
        """public abstract dev.ultreon.quantum.client.render.EntityTextures dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.getTextures()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def animate(self, arg0: 'EntityModelInstance', arg1: 'WorldRenderContext'):
        """public abstract void dev.ultreon.quantum.client.model.entity.renderer.EntityRenderer.animate(dev.ultreon.quantum.client.model.EntityModelInstance<E>,dev.ultreon.quantum.client.model.WorldRenderContext<E>)"""
        pass