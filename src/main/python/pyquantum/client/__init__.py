from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = __import_once__("pyquantum.registry")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.ClientRegistries as __ClientRegistries
__ClientRegistries = __ClientRegistries
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClientRegistries():
    """dev.ultreon.quantum.client.ClientRegistries"""
 
    @staticmethod
    def __wrap(java_value: __ClientRegistries) -> 'ClientRegistries':
        return ClientRegistries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientRegistries):
        """
        Dynamic initializer for ClientRegistries.
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
 
    # public static final dev.ultreon.quantum.registry.Registry<com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter> dev.ultreon.quantum.client.ClientRegistries.PARTICLE_EMITTER
    PARTICLE_EMITTER: 'registry.Registry' = __wrap(__registry.Registry.PARTICLE_EMITTER)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.render.RenderLayer> dev.ultreon.quantum.client.ClientRegistries.RENDER_LAYER
    RENDER_LAYER: 'registry.Registry' = __wrap(__registry.Registry.RENDER_LAYER)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.font.Font> dev.ultreon.quantum.client.ClientRegistries.FONT
    FONT: 'registry.Registry' = __wrap(__registry.Registry.FONT)

    # public static final dev.ultreon.quantum.registry.Registry<com.badlogic.gdx.graphics.g3d.particles.ParticleController> dev.ultreon.quantum.client.ClientRegistries.PARTICLE_CONTROLLER
    PARTICLE_CONTROLLER: 'registry.Registry' = __wrap(__registry.Registry.PARTICLE_CONTROLLER)

    # public static final dev.ultreon.quantum.registry.Registry<com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer<?, ?>> dev.ultreon.quantum.client.ClientRegistries.PARTICLE_CONTROLLER_RENDERER
    PARTICLE_CONTROLLER_RENDERER: 'registry.Registry' = __wrap(__registry.Registry.PARTICLE_CONTROLLER_RENDERER)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.gui.debug.DebugPage> dev.ultreon.quantum.client.ClientRegistries.DEBUG_PAGE
    DEBUG_PAGE: 'registry.Registry' = __wrap(__registry.Registry.DEBUG_PAGE)


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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.ClientRegistries()"""
        val = __ClientRegistries()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.ClientRegistries()"""
        val = __ClientRegistries()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

 
 
 
# CLASS: dev.ultreon.quantum.client.ClientRegistries
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = __import_once__("pyquantum.registry")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.ClientRegistries as __ClientRegistries
__ClientRegistries = __ClientRegistries
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClientRegistries():
    """dev.ultreon.quantum.client.ClientRegistries"""
 
    @staticmethod
    def __wrap(java_value: __ClientRegistries) -> 'ClientRegistries':
        return ClientRegistries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientRegistries):
        """
        Dynamic initializer for ClientRegistries.
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
 
    # public static final dev.ultreon.quantum.registry.Registry<com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter> dev.ultreon.quantum.client.ClientRegistries.PARTICLE_EMITTER
    PARTICLE_EMITTER: 'registry.Registry' = __wrap(__registry.Registry.PARTICLE_EMITTER)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.render.RenderLayer> dev.ultreon.quantum.client.ClientRegistries.RENDER_LAYER
    RENDER_LAYER: 'registry.Registry' = __wrap(__registry.Registry.RENDER_LAYER)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.font.Font> dev.ultreon.quantum.client.ClientRegistries.FONT
    FONT: 'registry.Registry' = __wrap(__registry.Registry.FONT)

    # public static final dev.ultreon.quantum.registry.Registry<com.badlogic.gdx.graphics.g3d.particles.ParticleController> dev.ultreon.quantum.client.ClientRegistries.PARTICLE_CONTROLLER
    PARTICLE_CONTROLLER: 'registry.Registry' = __wrap(__registry.Registry.PARTICLE_CONTROLLER)

    # public static final dev.ultreon.quantum.registry.Registry<com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer<?, ?>> dev.ultreon.quantum.client.ClientRegistries.PARTICLE_CONTROLLER_RENDERER
    PARTICLE_CONTROLLER_RENDERER: 'registry.Registry' = __wrap(__registry.Registry.PARTICLE_CONTROLLER_RENDERER)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.gui.debug.DebugPage> dev.ultreon.quantum.client.ClientRegistries.DEBUG_PAGE
    DEBUG_PAGE: 'registry.Registry' = __wrap(__registry.Registry.DEBUG_PAGE)


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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.ClientRegistries()"""
        val = __ClientRegistries()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.ClientRegistries()"""
        val = __ClientRegistries()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

 
 
 
# CLASS: dev.ultreon.quantum.client.ClientRegistries 
 
 
# CLASS: dev.ultreon.quantum.client.ServerData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import dev.ultreon.quantum.client.ServerData as __ServerData
__ServerData = __ServerData
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ServerData():
    """dev.ultreon.quantum.client.ServerData"""
 
    @staticmethod
    def __wrap(java_value: __ServerData) -> 'ServerData':
        return ServerData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerData):
        """
        Dynamic initializer for ServerData.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.ServerData.name()"""
        return str.__wrap(super(ServerData, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.ServerData.hashCode()"""
        return int.__wrap(super(ServerData, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.ServerData.equals(java.lang.Object)"""
        return bool.__wrap(super(__ServerData, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.ServerData.toString()"""
        return str.__wrap(super(ServerData, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.client.ServerData(java.lang.String,java.lang.String)"""
        val = __ServerData(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def address(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.ServerData.address()"""
        return str.__wrap(super(ServerData, self).address()) 
 
 
# CLASS: dev.ultreon.quantum.client.GameLibGDXWrapper
import dev.ultreon.quantum.client.GameLibGDXWrapper as __GameLibGDXWrapper
__GameLibGDXWrapper = __GameLibGDXWrapper
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GameLibGDXWrapper(pygdx.__ApplicationListener, pygdx.ApplicationListener):
    """dev.ultreon.quantum.client.GameLibGDXWrapper"""
 
    @staticmethod
    def __wrap(java_value: __GameLibGDXWrapper) -> 'GameLibGDXWrapper':
        return GameLibGDXWrapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameLibGDXWrapper):
        """
        Dynamic initializer for GameLibGDXWrapper.
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
    def resume(self):
        """public void dev.ultreon.quantum.client.GameLibGDXWrapper.resume()"""
        super(GameLibGDXWrapper, self).resume()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def render(self):
        """public void dev.ultreon.quantum.client.GameLibGDXWrapper.render()"""
        super(GameLibGDXWrapper, self).render()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def create(self):
        """public void dev.ultreon.quantum.client.GameLibGDXWrapper.create()"""
        super(GameLibGDXWrapper, self).create()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.GameLibGDXWrapper.dispose()"""
        super(GameLibGDXWrapper, self).dispose()

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
    def createInstance(arg0: 'String') -> 'GameLibGDXWrapper':
        """public static dev.ultreon.quantum.client.GameLibGDXWrapper dev.ultreon.quantum.client.GameLibGDXWrapper.createInstance(java.lang.String[])"""
        return GameLibGDXWrapper.__wrap(__GameLibGDXWrapper.createInstance(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.GameLibGDXWrapper.resize(int,int)"""
        super(__GameLibGDXWrapper, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def pause(self):
        """public void dev.ultreon.quantum.client.GameLibGDXWrapper.pause()"""
        super(GameLibGDXWrapper, self).pause() 
 
 
# CLASS: dev.ultreon.quantum.client.ClientResources
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
import dev.ultreon.quantum.client.ClientResources as __ClientResources
__ClientResources = __ClientResources
from builtins import type
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
import com.badlogic.gdx.graphics.g2d.BitmapFont as __BitmapFont
__BitmapFont = __BitmapFont
from builtins import int
 
class ClientResources():
    """dev.ultreon.quantum.client.ClientResources"""
 
    @staticmethod
    def __wrap(java_value: __ClientResources) -> 'ClientResources':
        return ClientResources(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientResources):
        """
        Dynamic initializer for ClientResources.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.ClientResources()"""
        val = __ClientResources()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def bitmapFont(arg0: 'Identifier') -> 'g2d.BitmapFont':
        """public static com.badlogic.gdx.graphics.g2d.BitmapFont dev.ultreon.quantum.client.ClientResources.bitmapFont(dev.ultreon.quantum.util.Identifier)"""
        return g2d.BitmapFont.__wrap(__ClientResources.bitmapFont(arg0))

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.ClientResources()"""
        val = __ClientResources()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.client.GameClipboard
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.awt.datatransfer.Clipboard as Clipboard
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.client.GameClipboard as __GameClipboard
__GameClipboard = __GameClipboard
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GameClipboard(__IClipboard, IClipboard):
    """dev.ultreon.quantum.client.GameClipboard"""
 
    @staticmethod
    def __wrap(java_value: __GameClipboard) -> 'GameClipboard':
        return GameClipboard(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameClipboard):
        """
        Dynamic initializer for GameClipboard.
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
    def __init__(self, arg0: 'Clipboard'):
        """public dev.ultreon.quantum.client.GameClipboard(java.awt.datatransfer.Clipboard)"""
        val = __GameClipboard(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def copy(self, arg0: str):
        """public void dev.ultreon.quantum.client.GameClipboard.copy(java.lang.String)"""
        super(__GameClipboard, self).copy(arg0)

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
    def copy(self, arg0: 'BufferedImage'):
        """public void dev.ultreon.quantum.client.GameClipboard.copy(java.awt.image.BufferedImage)"""
        super(__GameClipboard, self).copy(arg0)

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
    def paste(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.GameClipboard.paste()"""
        return str.__wrap(super(GameClipboard, self).paste())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.DevScreen
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import dev.ultreon.quantum.client.gui.Screen as __Screen
__Screen = __Screen
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.gui.Dialog as __Dialog
__Dialog = __Dialog
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.client.DevScreen as __DevScreen
__DevScreen = __DevScreen
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class DevScreen(client.__Screen, gui.Screen):
    """dev.ultreon.quantum.client.DevScreen"""
 
    @staticmethod
    def __wrap(java_value: __DevScreen) -> 'DevScreen':
        return DevScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DevScreen):
        """
        Dynamic initializer for DevScreen.
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
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'widget.UIContainer' = __wrap(__widget.UIContainer.ROOT)


    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__gui.Screen, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @property
    def directHovered(self) -> Widget:
        return Widget.__wrap(super(__Screen).directHovered())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(widget.Widget, self).isClickable())

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__widget.Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__widget.Widget, self).setBounds(arg0)

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__widget.Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def title(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canClose()"""
        return bool.__wrap(super(gui.Screen, self).canClose())

    @override
    @overload
    def getDialog(self) -> 'gui.Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'gui.Dialog'.__wrap(super(gui.Screen, self).getDialog())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__widget.Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(widget.UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(widget.Widget, self).getPreferredHeight())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool.__wrap(super(__gui.Screen, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(widget.Widget, self).getPreferredSize())

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__widget.Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.DevScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(__DevScreen, self).build(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).titleTranslation(arg0))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'.__wrap(super(gui.Screen, self).path())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(__gui.Screen, self).closeDialog(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

    @property
    def focused(self, value: 'widget.Widget'):
        super(__Screen).focused(value)

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(__Screen).parentScreen(value)

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(widget.Widget, self).componentRegistry())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(widget.Widget, self).getX())

    @override
    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(__gui.Screen, self).init(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__widget.Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__widget.Widget, self).y(__int.valueOf(arg0))

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool.__wrap(super(__gui.Screen, self).onClose(arg0))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).remove(arg0)

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__widget.Widget, self).height(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(widget.Widget, self).isEnabled())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__widget.Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(widget.Widget, self).isFocused())

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(__gui.Screen, self).showDialog(arg0)

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(__gui.Screen, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__widget.Widget, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__widget.Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'.__wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(__gui.Screen, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__widget.Widget, self).setPos(arg0)

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__widget.UIContainer, self).setLayout(arg0)

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__widget.Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'.__wrap(super(__gui.Screen, self).add(arg0))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.DevScreen.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__DevScreen, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool.__wrap(super(__gui.Screen, self).filesDropped(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__widget.Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).position(arg0))

    @override
    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool.__wrap(super(gui.Screen, self).back())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).bounds(arg0))

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canCloseWithEsc()"""
        return bool.__wrap(super(gui.Screen, self).canCloseWithEsc())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str.__wrap(super(gui.Screen, self).getName())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(widget.Widget, self).isHovered())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__widget.Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__widget.Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(__Screen).directHovered(value)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'.__wrap(super(gui.Screen, self).getTitle())

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__widget.Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__widget.Widget, self).onRevalidate(arg0)

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__widget.UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @property
    def focused(self) -> Widget:
        return Widget.__wrap(super(__Screen).focused())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(widget.Widget, self).getWidth())

    @property
    def parentScreen(self) -> Screen:
        return Screen.__wrap(super(__Screen).parentScreen())

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str.__wrap(super(gui.Screen, self).getRawTitle())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool.__wrap(super(gui.Screen, self).isHoveringClickable())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__widget.Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__widget.Widget, self).setSize(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.DebugRegistration
import dev.ultreon.quantum.client.DebugRegistration as __DebugRegistration
__DebugRegistration = __DebugRegistration
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DebugRegistration():
    """dev.ultreon.quantum.client.DebugRegistration"""
 
    @staticmethod
    def __wrap(java_value: __DebugRegistration) -> 'DebugRegistration':
        return DebugRegistration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DebugRegistration):
        """
        Dynamic initializer for DebugRegistration.
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
        def registerAutoFillers():
            """public static void dev.ultreon.quantum.client.DebugRegistration.registerAutoFillers()"""
            __DebugRegistration.registerAutoFillers()

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.DebugRegistration()"""
        val = __DebugRegistration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self):
        """public dev.ultreon.quantum.client.DebugRegistration()"""
        val = __DebugRegistration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.IntegratedServer
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
try:
    from pyquantum.client import player
except ImportError:
    player = __import_once__("pyquantum.client.player")

try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

try:
    from pyquantum import recipe
except ImportError:
    recipe = __import_once__("pyquantum.recipe")

import java.util.concurrent.ScheduledFuture as __ScheduledFuture
__ScheduledFuture = __ScheduledFuture
import java.util.stream.Stream as __Stream
__Stream = __Stream
import dev.ultreon.quantum.debug.profiler.Profiler as __Profiler
__Profiler = __Profiler
import dev.ultreon.quantum.server.QuantumServer as __QuantumServer
__QuantumServer = __QuantumServer
import java.util.Collection as Collection
try:
    from pyquantum import crash
except ImportError:
    crash = __import_once__("pyquantum.crash")

import dev.ultreon.quantum.server.player.ServerPlayer as __ServerPlayer
__ServerPlayer = __ServerPlayer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.ServerWorld as __ServerWorld
__ServerWorld = __ServerWorld
try:
    from pyquantum.debug import profiler
except ImportError:
    profiler = __import_once__("pyquantum.debug.profiler")

import java.util.concurrent.Callable as Callable
try:
    from pyquantum import gamerule
except ImportError:
    gamerule = __import_once__("pyquantum.gamerule")

from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.resources.ResourceManager as __ResourceManager
__ResourceManager = __ResourceManager
import java.util.concurrent.CompletableFuture as __CompletableFuture
__CompletableFuture = __CompletableFuture
import dev.ultreon.quantum.client.QuantumClient as __QuantumClient
__QuantumClient = __QuantumClient
import java.util.List as __List
__List = __List
import java.lang.Float as __float
import dev.ultreon.quantum.server.PlayerManager as __PlayerManager
__PlayerManager = __PlayerManager
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.server.ServerDisposable as __ServerDisposable
__ServerDisposable = __ServerDisposable
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.util.concurrent.CompletableFuture as CompletableFuture
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
import java.lang.Boolean as __boolean
import dev.ultreon.quantum.server.player.CachedPlayer as __CachedPlayer
__CachedPlayer = __CachedPlayer
from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.util.PollingExecutorService as __PollingExecutorService
__PollingExecutorService = __PollingExecutorService
import dev.ultreon.quantum.client.IntegratedServer as __IntegratedServer
__IntegratedServer = __IntegratedServer
import java.lang.Exception as Exception
import dev.ultreon.quantum.recipe.RecipeManager as __RecipeManager
__RecipeManager = __RecipeManager
import dev.ultreon.quantum.gamerule.GameRules as __GameRules
__GameRules = __GameRules
import java.lang.String as __string
import dev.ultreon.quantum.server.player.CacheablePlayer as __CacheablePlayer
__CacheablePlayer = __CacheablePlayer
import java.util.concurrent.ScheduledFuture as ScheduledFuture
import dev.ultreon.quantum.server.player.PermissionMap as __PermissionMap
__PermissionMap = __PermissionMap
from builtins import str
import dev.ultreon.quantum.world.WorldStorage as __WorldStorage
__WorldStorage = __WorldStorage
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Runnable as Runnable
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

from builtins import object
import dev.ultreon.quantum.network.Networker as __Networker
__Networker = __Networker
try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.util.UUID as __UUID
__UUID = __UUID
import dev.ultreon.quantum.api.commands.CommandSender as __CommandSender
__CommandSender = __CommandSender
import java.lang.Throwable as Throwable
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import java.util.Map as Map
import java.util.List as List
 
class IntegratedServer(pyquantum.__QuantumServer, server.QuantumServer):
    """dev.ultreon.quantum.client.IntegratedServer"""
 
    @staticmethod
    def __wrap(java_value: __IntegratedServer) -> 'IntegratedServer':
        return IntegratedServer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntegratedServer):
        """
        Dynamic initializer for IntegratedServer.
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
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.server.QuantumServer.LOGGER
    LOGGER: 'log.Logger' = __wrap(__log.Logger.LOGGER)


    @override
    @overload
    def execute(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.util.PollingExecutorService.execute(java.lang.Runnable)"""
        super(__util.PollingExecutorService, self).execute(arg0)

    @override
    @overload
    def crash(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.client.IntegratedServer.crash(dev.ultreon.quantum.crash.CrashLog)"""
        super(__IntegratedServer, self).crash(arg0)

    @overload
    def savePlayer(self):
        """public void dev.ultreon.quantum.client.IntegratedServer.savePlayer()"""
        super(IntegratedServer, self).savePlayer()

    @overload
    def getCacheablePlayer(self, arg0: 'UUID') -> 'player.CacheablePlayer':
        """public dev.ultreon.quantum.server.player.CacheablePlayer dev.ultreon.quantum.server.QuantumServer.getCacheablePlayer(java.util.UUID)"""
        return 'player.CacheablePlayer'.__wrap(super(__server.QuantumServer, self).getCacheablePlayer(arg0))

    @overload
    def getCacheablePlayer(self, arg0: str) -> 'player.CacheablePlayer':
        """public dev.ultreon.quantum.server.player.CacheablePlayer dev.ultreon.quantum.server.QuantumServer.getCacheablePlayer(java.lang.String)"""
        return 'player.CacheablePlayer'.__wrap(super(__server.QuantumServer, self).getCacheablePlayer(arg0))

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Callable') -> object:
        """public static <T> T dev.ultreon.quantum.server.QuantumServer.invokeAndWait(java.util.concurrent.Callable<T>)"""
        return object.__wrap(__QuantumServer.invokeAndWait(arg0))

    @override
    @overload
    def placePlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.client.IntegratedServer.placePlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__IntegratedServer, self).placePlayer(arg0)

    @staticmethod
    @overload
    def get() -> 'server.QuantumServer':
        """public static dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.server.QuantumServer.get()"""
        return server.QuantumServer.__wrap(__QuantumServer.get())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def pollAll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.pollAll()"""
        super(util.PollingExecutorService, self).pollAll()

    @override
    @overload
    def fatalCrash(self, arg0: 'Throwable'):
        """public void dev.ultreon.quantum.client.IntegratedServer.fatalCrash(java.lang.Throwable)"""
        super(__IntegratedServer, self).fatalCrash(arg0)

    @overload
    def submit(self, arg0: 'Runnable', arg1: object) -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable,T)"""
        return 'CompletableFuture'.__wrap(super(__util.PollingExecutorService, self).submit(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def invoke(arg0: 'Callable') -> 'CompletableFuture':
        """public static <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.server.QuantumServer.invoke(java.util.concurrent.Callable<T>)"""
        return CompletableFuture.__wrap(__QuantumServer.invoke(arg0))

    @override
    @overload
    def getWorld(self) -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.server.QuantumServer.getWorld()"""
        return 'world.ServerWorld'.__wrap(super(server.QuantumServer, self).getWorld())

    @override
    @overload
    def poll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.poll()"""
        super(util.PollingExecutorService, self).poll()

    @override
    @overload
    def getMaxPlayers(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getMaxPlayers()"""
        return int.__wrap(super(server.QuantumServer, self).getMaxPlayers())

    @overload
    def getClient(self) -> 'QuantumClient':
        """public dev.ultreon.quantum.client.QuantumClient dev.ultreon.quantum.client.IntegratedServer.getClient()"""
        return 'QuantumClient'.__wrap(super(IntegratedServer, self).getClient())

    @override
    @overload
    def isDedicated(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isDedicated()"""
        return bool.__wrap(super(server.QuantumServer, self).isDedicated())

    @override
    @overload
    def getDefaultPermissions(self) -> 'player.PermissionMap':
        """public dev.ultreon.quantum.server.player.PermissionMap dev.ultreon.quantum.server.QuantumServer.getDefaultPermissions()"""
        return 'player.PermissionMap'.__wrap(super(server.QuantumServer, self).getDefaultPermissions())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getPlayer(self, arg0: 'UUID') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.getPlayer(java.util.UUID)"""
        return 'player.ServerPlayer'.__wrap(super(__server.QuantumServer, self).getPlayer(arg0))

    @staticmethod
    @overload
    def invoke(arg0: 'Runnable') -> 'CompletableFuture':
        """public static java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.server.QuantumServer.invoke(java.lang.Runnable)"""
        return CompletableFuture.__wrap(__QuantumServer.invoke(arg0))

    @override
    @overload
    def getWorlds(self) -> 'Collection':
        """public java.util.Collection<? extends dev.ultreon.quantum.world.World> dev.ultreon.quantum.server.QuantumServer.getWorlds()"""
        return 'Collection'.__wrap(super(server.QuantumServer, self).getWorlds())

    @overload
    def schedule(self, arg0: 'Runnable', arg1: int, arg2: 'TimeUnit') -> 'ScheduledFuture':
        """public java.util.concurrent.ScheduledFuture<?> dev.ultreon.quantum.server.QuantumServer.schedule(java.lang.Runnable,long,java.util.concurrent.TimeUnit)"""
        return 'ScheduledFuture'.__wrap(super(__server.QuantumServer, self).schedule(arg0, __long.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def isOnServerThread() -> bool:
        """public static boolean dev.ultreon.quantum.server.QuantumServer.isOnServerThread()"""
        return bool.__wrap(__QuantumServer.isOnServerThread())

    @overload
    def getEntity(self, arg0: int, *arg1: 'entity.Entity') -> 'entity.Entity':
        """public final <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.server.QuantumServer.getEntity(int,T...)"""
        return 'entity.Entity'.__wrap(super(__server.QuantumServer, self).getEntity(__int.valueOf(arg0), arg1))

    @override
    @overload
    def getEntityRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getEntityRenderDistance()"""
        return int.__wrap(super(server.QuantumServer, self).getEntityRenderDistance())

    @overload
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__util.PollingExecutorService, self).invokeAny(arg0, __long.valueOf(arg1), arg2))

    @override
    @overload
    def isInitialChunksLoaded(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isInitialChunksLoaded()"""
        return bool.__wrap(super(server.QuantumServer, self).isInitialChunksLoaded())

    @overload
    def getWorld(self, arg0: 'Identifier') -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.server.QuantumServer.getWorld(dev.ultreon.quantum.util.Identifier)"""
        return 'world.ServerWorld'.__wrap(super(__server.QuantumServer, self).getWorld(arg0))

    @overload
    def invokeAny(self, arg0: 'Collection') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__util.PollingExecutorService, self).invokeAny(arg0))

    @overload
    def disposeOnClose(self, arg0: 'ServerDisposable') -> 'server.ServerDisposable':
        """public <T extends dev.ultreon.quantum.server.ServerDisposable> T dev.ultreon.quantum.server.QuantumServer.disposeOnClose(T)"""
        return 'server.ServerDisposable'.__wrap(super(__server.QuantumServer, self).disposeOnClose(arg0))

    @override
    @overload
    def getGameVersion(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.QuantumServer.getGameVersion()"""
        return str.__wrap(super(server.QuantumServer, self).getGameVersion())

    @override
    @overload
    def getStorage(self) -> 'world.WorldStorage':
        """public dev.ultreon.quantum.world.WorldStorage dev.ultreon.quantum.server.QuantumServer.getStorage()"""
        return 'world.WorldStorage'.__wrap(super(server.QuantumServer, self).getStorage())

    @override
    @overload
    def getPlayerManager(self) -> 'server.PlayerManager':
        """public dev.ultreon.quantum.server.PlayerManager dev.ultreon.quantum.server.QuantumServer.getPlayerManager()"""
        return 'server.PlayerManager'.__wrap(super(server.QuantumServer, self).getPlayerManager())

    @override
    @overload
    def getRecipeManager(self) -> 'recipe.RecipeManager':
        """public dev.ultreon.quantum.recipe.RecipeManager dev.ultreon.quantum.server.QuantumServer.getRecipeManager()"""
        return 'recipe.RecipeManager'.__wrap(super(server.QuantumServer, self).getRecipeManager())

    @override
    @overload
    def getHost(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.IntegratedServer.getHost()"""
        return 'UUID'.__wrap(super(IntegratedServer, self).getHost())

    @overload
    def loadPlayer(self, arg0: str, arg1: 'UUID', arg2: 'IConnection') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.loadPlayer(java.lang.String,java.util.UUID,dev.ultreon.quantum.network.system.IConnection)"""
        return 'player.ServerPlayer'.__wrap(super(__server.QuantumServer, self).loadPlayer(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPlayerCount(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getPlayerCount()"""
        return int.__wrap(super(server.QuantumServer, self).getPlayerCount())

    @overload
    def submit(self, arg0: 'Runnable') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable)"""
        return 'CompletableFuture'.__wrap(super(__util.PollingExecutorService, self).submit(arg0))

    @overload
    def hasPlayedBefore(self, arg0: 'CacheablePlayer') -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.hasPlayedBefore(dev.ultreon.quantum.server.player.CacheablePlayer)"""
        return bool.__wrap(super(__server.QuantumServer, self).hasPlayedBefore(arg0))

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isShutdown()"""
        return bool.__wrap(super(util.PollingExecutorService, self).isShutdown())

    @overload
    def openToLan(self):
        """public void dev.ultreon.quantum.client.IntegratedServer.openToLan()"""
        super(IntegratedServer, self).openToLan()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.IntegratedServer.toString()"""
        return str.__wrap(super(IntegratedServer, self).toString())

    @override
    @overload
    def getPlayersByName(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayersByName()"""
        return 'Map'.__wrap(super(server.QuantumServer, self).getPlayersByName())

    @override
    @overload
    def getOnlineTicks(self) -> int:
        """public long dev.ultreon.quantum.server.QuantumServer.getOnlineTicks()"""
        return int.__wrap(super(server.QuantumServer, self).getOnlineTicks())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getPlayersInChunk(self, arg0: 'ChunkPos') -> 'Stream':
        """public java.util.stream.Stream<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayersInChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Stream'.__wrap(super(__server.QuantumServer, self).getPlayersInChunk(arg0))

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.client.IntegratedServer.start()"""
        super(IntegratedServer, self).start()

    @override
    @overload
    def getPlayers(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayers()"""
        return 'Collection'.__wrap(super(server.QuantumServer, self).getPlayers())

    @override
    @overload
    def crash(self, arg0: 'Throwable'):
        """public void dev.ultreon.quantum.server.QuantumServer.crash(java.lang.Throwable)"""
        super(__server.QuantumServer, self).crash(arg0)

    @override
    @overload
    def onDisconnected(self, arg0: 'ServerPlayer', arg1: str):
        """public void dev.ultreon.quantum.server.QuantumServer.onDisconnected(dev.ultreon.quantum.server.player.ServerPlayer,java.lang.String)"""
        super(__server.QuantumServer, self).onDisconnected(arg0, arg1)

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Runnable'):
        """public static void dev.ultreon.quantum.server.QuantumServer.invokeAndWait(java.lang.Runnable)"""
        __QuantumServer.invokeAndWait(arg0)

    @overload
    def __init__(self, arg0: 'WorldStorage'):
        """public dev.ultreon.quantum.client.IntegratedServer(dev.ultreon.quantum.world.WorldStorage)"""
        val = __IntegratedServer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isIntegrated(self) -> bool:
        """public boolean dev.ultreon.quantum.client.IntegratedServer.isIntegrated()"""
        return bool.__wrap(super(IntegratedServer, self).isIntegrated())

    @overload
    def submit(self, arg0: 'Callable') -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'CompletableFuture'.__wrap(super(__util.PollingExecutorService, self).submit(arg0))

    @override
    @overload
    def shutdown(self):
        """public void dev.ultreon.quantum.client.IntegratedServer.shutdown()"""
        super(IntegratedServer, self).shutdown()

    @overload
    def invokeAll(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit)"""
        return 'List'.__wrap(super(__util.PollingExecutorService, self).invokeAll(arg0, __long.valueOf(arg1), arg2))

    @override
    @overload
    def isTerminated(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isTerminated()"""
        return bool.__wrap(super(util.PollingExecutorService, self).isTerminated())

    @staticmethod
    @overload
    def seconds2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.seconds2ticks(float)"""
        return int.__wrap(__QuantumServer.seconds2ticks(__float.valueOf(arg0)))

    @override
    @overload
    def onInitialChunksLoaded(self):
        """public void dev.ultreon.quantum.client.IntegratedServer.onInitialChunksLoaded()"""
        super(IntegratedServer, self).onInitialChunksLoaded()

    @override
    @overload
    def getNetworker(self) -> 'network.Networker':
        """public dev.ultreon.quantum.network.Networker dev.ultreon.quantum.server.QuantumServer.getNetworker()"""
        return 'network.Networker'.__wrap(super(server.QuantumServer, self).getNetworker())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def minutes2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.minutes2ticks(float)"""
        return int.__wrap(__QuantumServer.minutes2ticks(__float.valueOf(arg0)))

    @override
    @overload
    def getRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.client.IntegratedServer.getRenderDistance()"""
        return int.__wrap(super(IntegratedServer, self).getRenderDistance())

    @property
    def profiler(self) -> Profiler:
        return Profiler.__wrap(super(__PollingExecutorService).profiler())

    @override
    @overload
    def save(self, arg0: bool):
        """public void dev.ultreon.quantum.client.IntegratedServer.save(boolean) throws java.io.IOException"""
        super(__IntegratedServer, self).save(__boolean.valueOf(arg0))

    @override
    @overload
    def addPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.server.QuantumServer.addPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__server.QuantumServer, self).addPlayer(arg0)

    @override
    @overload
    def handleChunkLoadFailure(self, arg0: 'ChunkPos', arg1: str):
        """public void dev.ultreon.quantum.client.IntegratedServer.handleChunkLoadFailure(dev.ultreon.quantum.world.ChunkPos,java.lang.String)"""
        super(__IntegratedServer, self).handleChunkLoadFailure(arg0, arg1)

    @override
    @overload
    def getConsoleSender(self) -> 'commands.CommandSender':
        """public dev.ultreon.quantum.api.commands.CommandSender dev.ultreon.quantum.server.QuantumServer.getConsoleSender()"""
        return 'commands.CommandSender'.__wrap(super(server.QuantumServer, self).getConsoleSender())

    @override
    @overload
    def getPort(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getPort()"""
        return int.__wrap(super(server.QuantumServer, self).getPort())

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.client.IntegratedServer.close()"""
        super(IntegratedServer, self).close()

    @override
    @overload
    def handleWorldSaveError(self, arg0: 'Exception'):
        """public void dev.ultreon.quantum.client.IntegratedServer.handleWorldSaveError(java.lang.Exception)"""
        super(__IntegratedServer, self).handleWorldSaveError(arg0)

    @staticmethod
    @overload
    def hours2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.hours2ticks(float)"""
        return int.__wrap(__QuantumServer.hours2ticks(__float.valueOf(arg0)))

    @override
    @overload
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isRunning()"""
        return bool.__wrap(super(server.QuantumServer, self).isRunning())

    @override
    @overload
    def load(self):
        """public void dev.ultreon.quantum.server.QuantumServer.load() throws java.io.IOException"""
        super(server.QuantumServer, self).load()

    @override
    @overload
    def getResourceManager(self) -> 'resources.ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.server.QuantumServer.getResourceManager()"""
        return 'resources.ResourceManager'.__wrap(super(server.QuantumServer, self).getResourceManager())

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> dev.ultreon.quantum.util.PollingExecutorService.shutdownNow()"""
        return 'List'.__wrap(super(util.PollingExecutorService, self).shutdownNow())

    @override
    @overload
    def getCachedPlayers(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.server.player.CachedPlayer> dev.ultreon.quantum.server.QuantumServer.getCachedPlayers()"""
        return 'List'.__wrap(super(server.QuantumServer, self).getCachedPlayers())

    @overload
    def getEntity(self, arg0: 'UUID') -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.server.QuantumServer.getEntity(java.util.UUID)"""
        return 'entity.Entity'.__wrap(super(__server.QuantumServer, self).getEntity(arg0))

    @override
    @overload
    def getCurrentTps(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getCurrentTps()"""
        return int.__wrap(super(server.QuantumServer, self).getCurrentTps())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def run(self):
        """public void dev.ultreon.quantum.server.QuantumServer.run()"""
        super(server.QuantumServer, self).run()

    @overload
    def getCachedPlayer(self, arg0: str) -> 'player.CachedPlayer':
        """public dev.ultreon.quantum.server.player.CachedPlayer dev.ultreon.quantum.server.QuantumServer.getCachedPlayer(java.lang.String)"""
        return 'player.CachedPlayer'.__wrap(super(__server.QuantumServer, self).getCachedPlayer(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getPlayer(self, arg0: str) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.getPlayer(java.lang.String)"""
        return 'player.ServerPlayer'.__wrap(super(__server.QuantumServer, self).getPlayer(arg0))

    @overload
    def getCachedPlayer(self, arg0: 'UUID') -> 'player.CachedPlayer':
        """public dev.ultreon.quantum.server.player.CachedPlayer dev.ultreon.quantum.server.QuantumServer.getCachedPlayer(java.util.UUID)"""
        return 'player.CachedPlayer'.__wrap(super(__server.QuantumServer, self).getCachedPlayer(arg0))

    @overload
    def isOpenToLan(self) -> bool:
        """public boolean dev.ultreon.quantum.client.IntegratedServer.isOpenToLan()"""
        return bool.__wrap(super(IntegratedServer, self).isOpenToLan())

    @overload
    def invokeAll(self, arg0: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>)"""
        return 'List'.__wrap(super(__util.PollingExecutorService, self).invokeAll(arg0))

    @overload
    def loadPlayer(self, arg0: 'LocalPlayer'):
        """public void dev.ultreon.quantum.client.IntegratedServer.loadPlayer(dev.ultreon.quantum.client.player.LocalPlayer)"""
        super(__IntegratedServer, self).loadPlayer(arg0)

    @overload
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit') -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__util.PollingExecutorService, self).awaitTermination(__long.valueOf(arg0), arg1))

    @override
    @overload
    def sendChunk(self, arg0: 'ChunkPos', arg1: 'Chunk'):
        """public void dev.ultreon.quantum.server.QuantumServer.sendChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk) throws java.io.IOException"""
        super(__server.QuantumServer, self).sendChunk(arg0, arg1)

    @override
    @overload
    def getGameRules(self) -> 'gamerule.GameRules':
        """public dev.ultreon.quantum.gamerule.GameRules dev.ultreon.quantum.server.QuantumServer.getGameRules()"""
        return 'gamerule.GameRules'.__wrap(super(server.QuantumServer, self).getGameRules()) 
 
 
# CLASS: dev.ultreon.quantum.client.NullClipboard
from builtins import str
import dev.ultreon.quantum.client.IClipboard as __IClipboard
__IClipboard = __IClipboard
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.NullClipboard as __NullClipboard
__NullClipboard = __NullClipboard
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NullClipboard(__IClipboard, IClipboard):
    """dev.ultreon.quantum.client.NullClipboard"""
 
    @staticmethod
    def __wrap(java_value: __NullClipboard) -> 'NullClipboard':
        return NullClipboard(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NullClipboard):
        """
        Dynamic initializer for NullClipboard.
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
    def copy(self, arg0: str):
        """public void dev.ultreon.quantum.client.NullClipboard.copy(java.lang.String)"""
        super(__NullClipboard, self).copy(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def paste(self) -> str:
        """public default java.lang.String dev.ultreon.quantum.client.IClipboard.paste()"""
        return str.__wrap(super(IClipboard, self).paste())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.NullClipboard()"""
        val = __NullClipboard()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.NullClipboard()"""
        val = __NullClipboard()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def copy(self, arg0: 'BufferedImage'):
        """public void dev.ultreon.quantum.client.NullClipboard.copy(java.awt.image.BufferedImage)"""
        super(__NullClipboard, self).copy(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.RhinoExceptionScreen
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import dev.ultreon.quantum.client.gui.Screen as __Screen
__Screen = __Screen
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.client.RhinoExceptionScreen as __RhinoExceptionScreen
__RhinoExceptionScreen = __RhinoExceptionScreen
import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.gui.Dialog as __Dialog
__Dialog = __Dialog
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class RhinoExceptionScreen(client.__Screen, gui.Screen):
    """dev.ultreon.quantum.client.RhinoExceptionScreen"""
 
    @staticmethod
    def __wrap(java_value: __RhinoExceptionScreen) -> 'RhinoExceptionScreen':
        return RhinoExceptionScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RhinoExceptionScreen):
        """
        Dynamic initializer for RhinoExceptionScreen.
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
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'widget.UIContainer' = __wrap(__widget.UIContainer.ROOT)


    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__gui.Screen, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @property
    def directHovered(self) -> Widget:
        return Widget.__wrap(super(__Screen).directHovered())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(widget.Widget, self).isClickable())

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__widget.Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__widget.Widget, self).setBounds(arg0)

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__widget.Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def title(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.RhinoExceptionScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(__RhinoExceptionScreen, self).build(arg0)

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canClose()"""
        return bool.__wrap(super(gui.Screen, self).canClose())

    @override
    @overload
    def getDialog(self) -> 'gui.Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'gui.Dialog'.__wrap(super(gui.Screen, self).getDialog())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__widget.Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(widget.UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(widget.Widget, self).getPreferredHeight())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool.__wrap(super(__gui.Screen, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(widget.Widget, self).getPreferredSize())

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__widget.Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).titleTranslation(arg0))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'.__wrap(super(gui.Screen, self).path())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(__gui.Screen, self).closeDialog(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

    @property
    def focused(self, value: 'widget.Widget'):
        super(__Screen).focused(value)

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(__Screen).parentScreen(value)

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(widget.Widget, self).componentRegistry())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(widget.Widget, self).getX())

    @override
    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(__gui.Screen, self).init(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__widget.Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__widget.Widget, self).y(__int.valueOf(arg0))

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool.__wrap(super(__gui.Screen, self).onClose(arg0))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).remove(arg0)

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__widget.Widget, self).height(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(widget.Widget, self).isEnabled())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__widget.Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(widget.Widget, self).isFocused())

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(__gui.Screen, self).showDialog(arg0)

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(__gui.Screen, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__widget.Widget, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__widget.UIContainer, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__widget.Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'.__wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(__gui.Screen, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__widget.Widget, self).setPos(arg0)

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__widget.UIContainer, self).setLayout(arg0)

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__widget.Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.client.RhinoExceptionScreen(java.util.List<org.mozilla.javascript.RhinoException>)"""
        val = __RhinoExceptionScreen(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'.__wrap(super(__gui.Screen, self).add(arg0))

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool.__wrap(super(__gui.Screen, self).filesDropped(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__widget.Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).position(arg0))

    @override
    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool.__wrap(super(gui.Screen, self).back())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).bounds(arg0))

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canCloseWithEsc()"""
        return bool.__wrap(super(gui.Screen, self).canCloseWithEsc())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str.__wrap(super(gui.Screen, self).getName())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(widget.Widget, self).isHovered())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__widget.Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__widget.Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(__Screen).directHovered(value)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'.__wrap(super(gui.Screen, self).getTitle())

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__widget.Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__widget.Widget, self).onRevalidate(arg0)

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__widget.UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @property
    def focused(self) -> Widget:
        return Widget.__wrap(super(__Screen).focused())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(widget.Widget, self).getWidth())

    @property
    def parentScreen(self) -> Screen:
        return Screen.__wrap(super(__Screen).parentScreen())

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str.__wrap(super(gui.Screen, self).getRawTitle())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool.__wrap(super(gui.Screen, self).isHoveringClickable())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__widget.Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__widget.Widget, self).setSize(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.GameEnvironment
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.GameEnvironment as __GameEnvironment
__GameEnvironment = __GameEnvironment
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class GameEnvironment(__Enum, Enum):
    """dev.ultreon.quantum.client.GameEnvironment"""
 
    @staticmethod
    def __wrap(java_value: __GameEnvironment) -> 'GameEnvironment':
        return GameEnvironment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameEnvironment):
        """
        Dynamic initializer for GameEnvironment.
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
 
    # public static final dev.ultreon.quantum.client.GameEnvironment dev.ultreon.quantum.client.GameEnvironment.NORMAL
    NORMAL: 'GameEnvironment' = __wrap(__GameEnvironment.NORMAL)

    # public static final dev.ultreon.quantum.client.GameEnvironment dev.ultreon.quantum.client.GameEnvironment.PACKAGED
    PACKAGED: 'GameEnvironment' = __wrap(__GameEnvironment.PACKAGED)

    # public static final dev.ultreon.quantum.client.GameEnvironment dev.ultreon.quantum.client.GameEnvironment.UNKNOWN
    UNKNOWN: 'GameEnvironment' = __wrap(__GameEnvironment.UNKNOWN)

    # public static final dev.ultreon.quantum.client.GameEnvironment dev.ultreon.quantum.client.GameEnvironment.DEVELOPMENT
    DEVELOPMENT: 'GameEnvironment' = __wrap(__GameEnvironment.DEVELOPMENT)


    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'GameEnvironment':
        """public static dev.ultreon.quantum.client.GameEnvironment dev.ultreon.quantum.client.GameEnvironment.valueOf(java.lang.String)"""
        return GameEnvironment.__wrap(__GameEnvironment.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def values() -> List['GameEnvironment']:
        """public static dev.ultreon.quantum.client.GameEnvironment[] dev.ultreon.quantum.client.GameEnvironment.values()"""
        return List[GameEnvironment].__wrap(__GameEnvironment.values()) 
 
 
# CLASS: dev.ultreon.quantum.client.FontManager
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.client.font.Font as __Font
__Font = __Font
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.FontManager as __FontManager
__FontManager = __FontManager
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.client import font
except ImportError:
    font = __import_once__("pyquantum.client.font")

import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FontManager(pygdx.__Disposable, utils.Disposable):
    """dev.ultreon.quantum.client.FontManager"""
 
    @staticmethod
    def __wrap(java_value: __FontManager) -> 'FontManager':
        return FontManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FontManager):
        """
        Dynamic initializer for FontManager.
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
    def getFont(self, arg0: 'Identifier') -> 'font.Font':
        """public dev.ultreon.quantum.client.font.Font dev.ultreon.quantum.client.FontManager.getFont(dev.ultreon.quantum.util.Identifier)"""
        return 'font.Font'.__wrap(super(__FontManager, self).getFont(arg0))

    @overload
    def registerFonts(self, arg0: 'ResourceManager'):
        """public void dev.ultreon.quantum.client.FontManager.registerFonts(dev.ultreon.quantum.resources.ResourceManager)"""
        super(__FontManager, self).registerFonts(arg0)

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
    def registerFont(self, arg0: 'Identifier', arg1: 'Font') -> 'font.Font':
        """public dev.ultreon.quantum.client.font.Font dev.ultreon.quantum.client.FontManager.registerFont(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.font.Font)"""
        return 'font.Font'.__wrap(super(__FontManager, self).registerFont(arg0, arg1))

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

    @staticmethod
    @overload
    def get() -> 'FontManager':
        """public static dev.ultreon.quantum.client.FontManager dev.ultreon.quantum.client.FontManager.get()"""
        return FontManager.__wrap(__FontManager.get())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.FontManager.dispose()"""
        super(FontManager, self).dispose()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.Metadata
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.client.Metadata as __Metadata
__Metadata = __Metadata
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Metadata():
    """dev.ultreon.quantum.client.Metadata"""
 
    @staticmethod
    def __wrap(java_value: __Metadata) -> 'Metadata':
        return Metadata(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Metadata):
        """
        Dynamic initializer for Metadata.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.Metadata()"""
        val = __Metadata()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @staticmethod
    @overload
    def get() -> 'Metadata':
        """public static dev.ultreon.quantum.client.Metadata dev.ultreon.quantum.client.Metadata.get()"""
        return Metadata.__wrap(__Metadata.get())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.Metadata()"""
        val = __Metadata()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.client.ClientModInit
import dev.ultreon.quantum.client.ClientModInit as __ClientModInit
__ClientModInit = __ClientModInit
from abc import abstractmethod, ABC
 
class ClientModInit(ABC):
    """dev.ultreon.quantum.client.ClientModInit"""
 
    @staticmethod
    def __wrap(java_value: __ClientModInit) -> 'ClientModInit':
        return ClientModInit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientModInit):
        """
        Dynamic initializer for ClientModInit.
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
    def onInitializeClient(self, ):
        """public abstract void dev.ultreon.quantum.client.ClientModInit.onInitializeClient()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.CrashScreen
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import dev.ultreon.quantum.client.gui.Screen as __Screen
__Screen = __Screen
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import dev.ultreon.quantum.client.CrashScreen as __CrashScreen
__CrashScreen = __CrashScreen
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.gui.Dialog as __Dialog
__Dialog = __Dialog
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class CrashScreen(client.__Screen, gui.Screen):
    """dev.ultreon.quantum.client.CrashScreen"""
 
    @staticmethod
    def __wrap(java_value: __CrashScreen) -> 'CrashScreen':
        return CrashScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CrashScreen):
        """
        Dynamic initializer for CrashScreen.
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
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'widget.UIContainer' = __wrap(__widget.UIContainer.ROOT)


    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__gui.Screen, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @property
    def directHovered(self) -> Widget:
        return Widget.__wrap(super(__Screen).directHovered())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(widget.Widget, self).isClickable())

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__widget.Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__widget.Widget, self).setBounds(arg0)

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.CrashScreen.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__CrashScreen, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__widget.Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def title(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.CrashScreen.canCloseWithEsc()"""
        return bool.__wrap(super(CrashScreen, self).canCloseWithEsc())

    @override
    @overload
    def getDialog(self) -> 'gui.Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'gui.Dialog'.__wrap(super(gui.Screen, self).getDialog())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__widget.Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(widget.UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(widget.Widget, self).getPreferredHeight())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool.__wrap(super(__gui.Screen, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(widget.Widget, self).getPreferredSize())

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__widget.Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).titleTranslation(arg0))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'.__wrap(super(gui.Screen, self).path())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(__gui.Screen, self).closeDialog(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

    @property
    def focused(self, value: 'widget.Widget'):
        super(__Screen).focused(value)

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(__Screen).parentScreen(value)

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(widget.Widget, self).componentRegistry())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(widget.Widget, self).getX())

    @override
    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(__gui.Screen, self).init(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__widget.Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__widget.Widget, self).y(__int.valueOf(arg0))

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool.__wrap(super(__gui.Screen, self).onClose(arg0))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).remove(arg0)

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__widget.Widget, self).height(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(widget.Widget, self).isEnabled())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__widget.Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(widget.Widget, self).isFocused())

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(__gui.Screen, self).showDialog(arg0)

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(__gui.Screen, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__widget.Widget, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__widget.Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'.__wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(__gui.Screen, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__widget.Widget, self).setPos(arg0)

    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.client.CrashScreen(java.util.List<dev.ultreon.quantum.crash.CrashLog>)"""
        val = __CrashScreen(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__widget.UIContainer, self).setLayout(arg0)

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__widget.Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'.__wrap(super(__gui.Screen, self).add(arg0))

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool.__wrap(super(__gui.Screen, self).filesDropped(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__widget.Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).position(arg0))

    @override
    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool.__wrap(super(gui.Screen, self).back())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).bounds(arg0))

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str.__wrap(super(gui.Screen, self).getName())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(widget.Widget, self).isHovered())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__widget.Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__widget.Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(__Screen).directHovered(value)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.CrashScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(__CrashScreen, self).build(arg0)

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'.__wrap(super(gui.Screen, self).getTitle())

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__widget.Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__widget.Widget, self).onRevalidate(arg0)

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__widget.UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @property
    def focused(self) -> Widget:
        return Widget.__wrap(super(__Screen).focused())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(widget.Widget, self).getWidth())

    @property
    def parentScreen(self) -> Screen:
        return Screen.__wrap(super(__Screen).parentScreen())

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str.__wrap(super(gui.Screen, self).getRawTitle())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool.__wrap(super(gui.Screen, self).isHoveringClickable())

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.CrashScreen.canClose()"""
        return bool.__wrap(super(CrashScreen, self).canClose())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__widget.Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__widget.Widget, self).setSize(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.IClipboard
from builtins import str
import dev.ultreon.quantum.client.IClipboard as __IClipboard
__IClipboard = __IClipboard
import java.lang.String as __String
__String = __String
import java.awt.image.BufferedImage as BufferedImage
from abc import abstractmethod, ABC
 
class IClipboard(ABC):
    """dev.ultreon.quantum.client.IClipboard"""
 
    @staticmethod
    def __wrap(java_value: __IClipboard) -> 'IClipboard':
        return IClipboard(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IClipboard):
        """
        Dynamic initializer for IClipboard.
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
    def copy(self, arg0: str):
        """public abstract void dev.ultreon.quantum.client.IClipboard.copy(java.lang.String)"""
        pass

    @abstractmethod
    def copy(self, arg0: 'BufferedImage'):
        """public abstract void dev.ultreon.quantum.client.IClipboard.copy(java.awt.image.BufferedImage)"""
        pass

    @overload
    def paste(self) -> str:
        """public default java.lang.String dev.ultreon.quantum.client.IClipboard.paste()"""
        return str.__wrap(super(IClipboard, self).paste()) 
 
 
# CLASS: dev.ultreon.quantum.client.DisposableContainer
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import dev.ultreon.quantum.client.DisposableContainer as __DisposableContainer
__DisposableContainer = __DisposableContainer
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
 
class DisposableContainer(ABC, pygdx.__Disposable, utils.Disposable):
    """dev.ultreon.quantum.client.DisposableContainer"""
 
    @staticmethod
    def __wrap(java_value: __DisposableContainer) -> 'DisposableContainer':
        return DisposableContainer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DisposableContainer):
        """
        Dynamic initializer for DisposableContainer.
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
    def deferDispose(self, arg0: 'Disposable'):
        """public abstract <T extends com.badlogic.gdx.utils.Disposable> T dev.ultreon.quantum.client.DisposableContainer.deferDispose(T)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.User
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.User as __User
__User = __User
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class User():
    """dev.ultreon.quantum.client.User"""
 
    @staticmethod
    def __wrap(java_value: __User) -> 'User':
        return User(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __User):
        """
        Dynamic initializer for User.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.User.hashCode()"""
        return int.__wrap(super(User, self).hashCode())

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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.User(java.lang.String)"""
        val = __User(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.User.name()"""
        return str.__wrap(super(User, self).name())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.User.toString()"""
        return str.__wrap(super(User, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.User.equals(java.lang.Object)"""
        return bool.__wrap(super(__User, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.InternalApi
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import dev.ultreon.quantum.client.InternalApi as __InternalApi
__InternalApi = __InternalApi
from abc import abstractmethod, ABC
 
class InternalApi(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.client.InternalApi"""
 
    @staticmethod
    def __wrap(java_value: __InternalApi) -> 'InternalApi':
        return InternalApi(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InternalApi):
        """
        Dynamic initializer for InternalApi.
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
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.GameRenderer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

try:
    from pyquantum.client.render import pipeline
except ImportError:
    pipeline = __import_once__("pyquantum.client.render.pipeline")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.GameRenderer as __GameRenderer
__GameRenderer = __GameRenderer
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

import com.badlogic.gdx.graphics.g3d.utils.RenderContext as __RenderContext
__RenderContext = __RenderContext
from builtins import int
 
class GameRenderer(pygdx.__Disposable, utils.Disposable):
    """dev.ultreon.quantum.client.GameRenderer"""
 
    @staticmethod
    def __wrap(java_value: __GameRenderer) -> 'GameRenderer':
        return GameRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameRenderer):
        """
        Dynamic initializer for GameRenderer.
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
    def __init__(self, arg0: 'QuantumClient', arg1: 'ModelBatch', arg2: 'RenderPipeline'):
        """public dev.ultreon.quantum.client.GameRenderer(dev.ultreon.quantum.client.QuantumClient,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.render.pipeline.RenderPipeline)"""
        val = __GameRenderer(arg0, arg1, arg2)
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

    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.GameRenderer.resize(int,int)"""
        super(__GameRenderer, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def render(self, arg0: 'Renderer', arg1: float):
        """public void dev.ultreon.quantum.client.GameRenderer.render(dev.ultreon.quantum.client.gui.Renderer,float)"""
        super(__GameRenderer, self).render(arg0, __float.valueOf(arg1))

    @overload
    def getContext(self) -> 'utils.RenderContext':
        """public com.badlogic.gdx.graphics.g3d.utils.RenderContext dev.ultreon.quantum.client.GameRenderer.getContext()"""
        return 'utils.RenderContext'.__wrap(super(GameRenderer, self).getContext())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.GameRenderer.dispose()"""
        super(GameRenderer, self).dispose()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.OutOfMemoryScreen
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import dev.ultreon.quantum.client.gui.Screen as __Screen
__Screen = __Screen
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.gui.Dialog as __Dialog
__Dialog = __Dialog
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.client.OutOfMemoryScreen as __OutOfMemoryScreen
__OutOfMemoryScreen = __OutOfMemoryScreen
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class OutOfMemoryScreen(client.__Screen, gui.Screen):
    """dev.ultreon.quantum.client.OutOfMemoryScreen"""
 
    @staticmethod
    def __wrap(java_value: __OutOfMemoryScreen) -> 'OutOfMemoryScreen':
        return OutOfMemoryScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OutOfMemoryScreen):
        """
        Dynamic initializer for OutOfMemoryScreen.
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
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'widget.UIContainer' = __wrap(__widget.UIContainer.ROOT)


    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__gui.Screen, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @property
    def directHovered(self) -> Widget:
        return Widget.__wrap(super(__Screen).directHovered())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(widget.Widget, self).isClickable())

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__widget.Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__widget.Widget, self).setBounds(arg0)

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__widget.Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def title(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canClose()"""
        return bool.__wrap(super(gui.Screen, self).canClose())

    @override
    @overload
    def getDialog(self) -> 'gui.Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'gui.Dialog'.__wrap(super(gui.Screen, self).getDialog())

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__widget.Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(widget.UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(widget.Widget, self).getPreferredHeight())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool.__wrap(super(__gui.Screen, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(widget.Widget, self).getPreferredSize())

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__widget.Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).titleTranslation(arg0))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'.__wrap(super(gui.Screen, self).path())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(__gui.Screen, self).closeDialog(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

    @property
    def focused(self, value: 'widget.Widget'):
        super(__Screen).focused(value)

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(__Screen).parentScreen(value)

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(widget.Widget, self).componentRegistry())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(widget.Widget, self).getX())

    @override
    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(__gui.Screen, self).init(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__widget.Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__widget.Widget, self).y(__int.valueOf(arg0))

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool.__wrap(super(__gui.Screen, self).onClose(arg0))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).remove(arg0)

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__widget.Widget, self).height(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(widget.Widget, self).isEnabled())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__widget.Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(widget.Widget, self).isFocused())

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(__gui.Screen, self).showDialog(arg0)

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(__gui.Screen, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__widget.Widget, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__widget.UIContainer, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__widget.Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'.__wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(__gui.Screen, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__widget.Widget, self).setPos(arg0)

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__widget.UIContainer, self).setLayout(arg0)

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__widget.Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'.__wrap(super(__gui.Screen, self).add(arg0))

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool.__wrap(super(__gui.Screen, self).filesDropped(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__widget.Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).position(arg0))

    @override
    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool.__wrap(super(gui.Screen, self).back())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).bounds(arg0))

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canCloseWithEsc()"""
        return bool.__wrap(super(gui.Screen, self).canCloseWithEsc())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str.__wrap(super(gui.Screen, self).getName())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(widget.Widget, self).isHovered())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__widget.Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__widget.Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(__Screen).directHovered(value)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'.__wrap(super(gui.Screen, self).getTitle())

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__widget.Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__widget.Widget, self).onRevalidate(arg0)

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__widget.UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @property
    def focused(self) -> Widget:
        return Widget.__wrap(super(__Screen).focused())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(widget.Widget, self).getWidth())

    @property
    def parentScreen(self) -> Screen:
        return Screen.__wrap(super(__Screen).parentScreen())

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str.__wrap(super(gui.Screen, self).getRawTitle())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool.__wrap(super(gui.Screen, self).isHoveringClickable())

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.OutOfMemoryScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(__OutOfMemoryScreen, self).build(arg0)

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__widget.Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__widget.Widget, self).setSize(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.Screenshot
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from builtins import str
import dev.ultreon.quantum.client.Screenshot as __Screenshot
__Screenshot = __Screenshot
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.nio.file.Path as Path
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap
__Pixmap = __Pixmap
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class Screenshot():
    """dev.ultreon.quantum.client.Screenshot"""
 
    @staticmethod
    def __wrap(java_value: __Screenshot) -> 'Screenshot':
        return Screenshot(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Screenshot):
        """
        Dynamic initializer for Screenshot.
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
    def dispose(self):
        """public void dev.ultreon.quantum.client.Screenshot.dispose()"""
        super(Screenshot, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def save(self, arg0: 'Path'):
        """public void dev.ultreon.quantum.client.Screenshot.save(java.nio.file.Path)"""
        super(__Screenshot, self).save(arg0)

    @overload
    def __init__(self, arg0: 'Pixmap'):
        """public dev.ultreon.quantum.client.Screenshot(com.badlogic.gdx.graphics.Pixmap)"""
        val = __Screenshot(arg0)
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

    @overload
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.Screenshot.isDisposed()"""
        return bool.__wrap(super(Screenshot, self).isDisposed())

    @staticmethod
    @overload
    def grab(arg0: int, arg1: int) -> 'Screenshot':
        """public static dev.ultreon.quantum.client.Screenshot dev.ultreon.quantum.client.Screenshot.grab(int,int)"""
        return Screenshot.__wrap(__Screenshot.grab(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getPixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap dev.ultreon.quantum.client.Screenshot.getPixmap()"""
        return 'graphics.Pixmap'.__wrap(super(Screenshot, self).getPixmap())

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
    def save(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.Screenshot.save(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__Screenshot, self).save(arg0))

    @overload
    def saveAndDispose(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.Screenshot.saveAndDispose(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__Screenshot, self).saveAndDispose(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.HardwareMonitor
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.HardwareMonitor as __HardwareMonitor
__HardwareMonitor = __HardwareMonitor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HardwareMonitor():
    """dev.ultreon.quantum.client.HardwareMonitor"""
 
    @staticmethod
    def __wrap(java_value: __HardwareMonitor) -> 'HardwareMonitor':
        return HardwareMonitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HardwareMonitor):
        """
        Dynamic initializer for HardwareMonitor.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.HardwareMonitor()"""
        val = __HardwareMonitor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

        @staticmethod
        @overload
        def start():
            """public static synchronized void dev.ultreon.quantum.client.HardwareMonitor.start()"""
            __HardwareMonitor.start()

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.HardwareMonitor()"""
        val = __HardwareMonitor()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.QuantumClient
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.IClipboard as __IClipboard
__IClipboard = __IClipboard
import dev.ultreon.quantum.client.item.ItemRenderer as __ItemRenderer
__ItemRenderer = __ItemRenderer
try:
    from pyquantum.client import player
except ImportError:
    player = __import_once__("pyquantum.client.player")

import java.lang.AutoCloseable as __AutoCloseable
__AutoCloseable = __AutoCloseable
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import dev.ultreon.quantum.debug.profiler.Profiler as __Profiler
__Profiler = __Profiler
import java.util.concurrent.ExecutorService as __ExecutorService
__ExecutorService = __ExecutorService
try:
    from pyquantum import crash
except ImportError:
    crash = __import_once__("pyquantum.crash")

import java.util.concurrent.Callable as Callable
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.client.util.GG as __GG
__GG = __GG
import dev.ultreon.quantum.resources.ResourceManager as __ResourceManager
__ResourceManager = __ResourceManager
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import java.util.concurrent.CompletableFuture as __CompletableFuture
__CompletableFuture = __CompletableFuture
try:
    from pyquantum.client import multiplayer
except ImportError:
    multiplayer = __import_once__("pyquantum.client.multiplayer")

from builtins import float
import com.badlogic.gdx.graphics.g3d.Environment as __Environment
__Environment = __Environment
try:
    from pyquantum.client.render import pipeline
except ImportError:
    pipeline = __import_once__("pyquantum.client.render.pipeline")

try:
    from pyquantum.client import registry
except ImportError:
    registry = __import_once__("pyquantum.client.registry")

from typing import List
import java.lang.Float as __float
try:
    from pyquantum.client import sound
except ImportError:
    sound = __import_once__("pyquantum.client.sound")

import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

try:
    from pyquantum.client import font
except ImportError:
    font = __import_once__("pyquantum.client.font")

import dev.ultreon.quantum.client.gui.NotifyManager as __NotifyManager
__NotifyManager = __NotifyManager
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.util.concurrent.CompletableFuture as CompletableFuture
import dev.ultreon.quantum.client.atlas.TextureAtlas as __TextureAtlas
__TextureAtlas = __TextureAtlas
from builtins import int
import dev.ultreon.quantum.client.gui.Screen as __Screen
__Screen = __Screen
import dev.ultreon.quantum.client.font.Font as __Font
__Font = __Font
from builtins import type
try:
    from pyquantum.client import atlas
except ImportError:
    atlas = __import_once__("pyquantum.client.atlas")

import dev.ultreon.quantum.network.system.IConnection as __IConnection
__IConnection = __IConnection
import dev.ultreon.quantum.client.management.MaterialManager as __MaterialManager
__MaterialManager = __MaterialManager
import dev.ultreon.quantum.client.management.ShaderProgramManager as __ShaderProgramManager
__ShaderProgramManager = __ShaderProgramManager
import java.lang.String as __string
try:
    from pyquantum.client import management
except ImportError:
    management = __import_once__("pyquantum.client.management")

import dev.ultreon.libs.datetime.v0.Duration as __Duration
__Duration = __Duration
import dev.ultreon.quantum.client.GameEnvironment as __GameEnvironment
__GameEnvironment = __GameEnvironment
import java.util.concurrent.ScheduledFuture as ScheduledFuture
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import dev.ultreon.quantum.client.Metadata as __Metadata
__Metadata = __Metadata
import java.lang.Runnable as Runnable
try:
    from pyquantum.client.gui import debug
except ImportError:
    debug = __import_once__("pyquantum.client.gui.debug")

import dev.ultreon.quantum.client.model.block.BlockModel as __BlockModel
__BlockModel = __BlockModel
import java.lang.AutoCloseable as AutoCloseable
from builtins import object
import dev.ultreon.quantum.client.player.LocalPlayer as __LocalPlayer
__LocalPlayer = __LocalPlayer
import dev.ultreon.quantum.client.player.SkinManager as __SkinManager
__SkinManager = __SkinManager
try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

import dev.ultreon.quantum.client.ServerData as __ServerData
__ServerData = __ServerData
import dev.ultreon.quantum.client.gui.debug.DebugOverlay as __DebugOverlay
__DebugOverlay = __DebugOverlay
try:
    from pyquantum.client import item
except ImportError:
    item = __import_once__("pyquantum.client.item")

import dev.ultreon.quantum.client.gui.Renderer as __Renderer
__Renderer = __Renderer
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import dev.ultreon.quantum.client.gui.Hud as __Hud
__Hud = __Hud
import dev.ultreon.quantum.client.management.ShaderProviderManager as __ShaderProviderManager
__ShaderProviderManager = __ShaderProviderManager
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

import dev.ultreon.quantum.GameWindow as __GameWindow
__GameWindow = __GameWindow
try:
    from pyquantum.client import util
except ImportError:
    util = __import_once__("pyquantum.client.util")

import dev.ultreon.quantum.client.config.ClientConfig as __ClientConfig
__ClientConfig = __ClientConfig
import java.util.List as List
import dev.ultreon.quantum.client.input.TouchPoint as __TouchPoint
__TouchPoint = __TouchPoint
import java.nio.file.Path as __Path
__Path = __Path
import java.util.concurrent.ScheduledFuture as __ScheduledFuture
__ScheduledFuture = __ScheduledFuture
import dev.ultreon.quantum.client.world.ClientWorld as __ClientWorld
__ClientWorld = __ClientWorld
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import java.util.Collection as Collection
import dev.ultreon.quantum.client.registry.EntityModelRegistry as __EntityModelRegistry
__EntityModelRegistry = __EntityModelRegistry
import dev.ultreon.quantum.client.input.GameInput as __GameInput
__GameInput = __GameInput
try:
    from pyquantum.client.model import block
except ImportError:
    block = __import_once__("pyquantum.client.model.block")

try:
    from pyquantum.client import audio
except ImportError:
    audio = __import_once__("pyquantum.client.audio")

import com.badlogic.gdx.math.GridPoint2 as __GridPoint2
__GridPoint2 = __GridPoint2
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.client.world.WorldRenderer as __WorldRenderer
__WorldRenderer = __WorldRenderer
try:
    from pyquantum.debug import profiler
except ImportError:
    profiler = __import_once__("pyquantum.debug.profiler")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.util.HitResult as __HitResult
__HitResult = __HitResult
import dev.ultreon.quantum.util.Shutdownable as __Shutdownable
__Shutdownable = __Shutdownable
import java.lang.Double as __double
import dev.ultreon.quantum.client.input.GameCamera as __GameCamera
__GameCamera = __GameCamera
from builtins import bool
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

try:
    from pyquantum.client import texture
except ImportError:
    texture = __import_once__("pyquantum.client.texture")

try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

import dev.ultreon.quantum.client.QuantumClient as __QuantumClient
__QuantumClient = __QuantumClient
try:
    from pyquantum.client import config
except ImportError:
    config = __import_once__("pyquantum.client.config")

import java.util.List as __List
__List = __List
import dev.ultreon.quantum.client.config.ConfigScreenFactory as __ConfigScreenFactory
__ConfigScreenFactory = __ConfigScreenFactory
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.User as __User
__User = __User
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

import java.lang.Boolean as __boolean
import dev.ultreon.quantum.client.config.GameSettings as __GameSettings
__GameSettings = __GameSettings
import dev.ultreon.quantum.client.texture.TextureManager as __TextureManager
__TextureManager = __TextureManager
import dev.ultreon.quantum.util.PollingExecutorService as __PollingExecutorService
__PollingExecutorService = __PollingExecutorService
import dev.ultreon.quantum.client.IntegratedServer as __IntegratedServer
__IntegratedServer = __IntegratedServer
try:
    from pycorelibs.datetime import v0
except ImportError:
    v0 = __import_once__("pycorelibs.datetime.v0")

import dev.ultreon.quantum.client.registry.EntityRendererRegistry as __EntityRendererRegistry
__EntityRendererRegistry = __EntityRendererRegistry
import dev.ultreon.quantum.client.input.PlayerInput as __PlayerInput
__PlayerInput = __PlayerInput
from builtins import str
import dev.ultreon.quantum.world.WorldStorage as __WorldStorage
__WorldStorage = __WorldStorage
import dev.ultreon.quantum.client.sound.ClientSoundRegistry as __ClientSoundRegistry
__ClientSoundRegistry = __ClientSoundRegistry
try:
    from pyquantum.debug import inspect
except ImportError:
    inspect = __import_once__("pyquantum.debug.inspect")

from pyquantum_helper import override
import dev.ultreon.quantum.util.BlockHitResult as __BlockHitResult
__BlockHitResult = __BlockHitResult
import java.lang.Object as __object
import dev.ultreon.quantum.client.util.PlayerView as __PlayerView
__PlayerView = __PlayerView
import java.nio.file.Path as Path
import com.badlogic.gdx.assets.AssetManager as __AssetManager
__AssetManager = __AssetManager
import dev.ultreon.quantum.debug.inspect.InspectionRoot as __InspectionRoot
__InspectionRoot = __InspectionRoot
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as __RenderPipeline
__RenderPipeline = __RenderPipeline
import dev.ultreon.quantum.client.multiplayer.MultiplayerData as __MultiplayerData
__MultiplayerData = __MultiplayerData
import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum.client import input
except ImportError:
    input = __import_once__("pyquantum.client.input")

import java.lang.Throwable as Throwable
import java.lang.Integer as __int
try:
    from pyquantum.client import rpc
except ImportError:
    rpc = __import_once__("pyquantum.client.rpc")

 
class QuantumClient(pyquantum.__PollingExecutorService, util.PollingExecutorService, client.__DeferredDisposable, util.DeferredDisposable):
    """dev.ultreon.quantum.client.QuantumClient"""
 
    @staticmethod
    def __wrap(java_value: __QuantumClient) -> 'QuantumClient':
        return QuantumClient(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __QuantumClient):
        """
        Dynamic initializer for QuantumClient.
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
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.client.QuantumClient.LOGGER
    LOGGER: 'log.Logger' = __wrap(__log.Logger.LOGGER)

    # public static final dev.ultreon.quantum.debug.profiler.Profiler dev.ultreon.quantum.client.QuantumClient.PROFILER
    PROFILER: 'profiler.Profiler' = __wrap(__profiler.Profiler.PROFILER)


    @property
    def serverData(self) -> ServerData:
        return ServerData.__wrap(super(__QuantumClient).serverData())

    @overload
    def getResourceManager(self) -> 'resources.ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.client.QuantumClient.getResourceManager()"""
        return 'resources.ResourceManager'.__wrap(super(QuantumClient, self).getResourceManager())

    @override
    @overload
    def execute(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.util.PollingExecutorService.execute(java.lang.Runnable)"""
        super(__util.PollingExecutorService, self).execute(arg0)

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Runnable'):
        """public static void dev.ultreon.quantum.client.QuantumClient.invokeAndWait(java.lang.Runnable)"""
        __QuantumClient.invokeAndWait(arg0)

    @staticmethod
    @overload
    def isPackaged() -> bool:
        """public static boolean dev.ultreon.quantum.client.QuantumClient.isPackaged()"""
        return bool.__wrap(__QuantumClient.isPackaged())

    @property
    def renderer(self) -> Renderer:
        return Renderer.__wrap(super(__QuantumClient).renderer())

    @property
    def player(self) -> LocalPlayer:
        return LocalPlayer.__wrap(super(__QuantumClient).player())

    @overload
    def startWorld(self, arg0: 'Path'):
        """public void dev.ultreon.quantum.client.QuantumClient.startWorld(java.nio.file.Path)"""
        super(__QuantumClient, self).startWorld(arg0)

    @override
    @overload
    def shutdown(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.shutdown()"""
        super(util.PollingExecutorService, self).shutdown()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @property
    def integratedServer(self, value: 'IntegratedServer'):
        super(__QuantumClient).integratedServer(value)

    @overload
    def startIntegratedServer(self):
        """public void dev.ultreon.quantum.client.QuantumClient.startIntegratedServer()"""
        super(QuantumClient, self).startIntegratedServer()

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void dev.ultreon.quantum.client.QuantumClient.main(java.lang.String[])"""
        __QuantumClient.main(arg0)

    @property
    def notifications(self, value: 'gui.NotifyManager'):
        super(__QuantumClient).notifications(value)

    @staticmethod
    @overload
    def getConfigDir() -> 'files.FileHandle':
        """public static com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.QuantumClient.getConfigDir()"""
        return files.FileHandle.__wrap(__QuantumClient.getConfigDir())

    @property
    def inspection(self) -> InspectionRoot:
        return InspectionRoot.__wrap(super(__QuantumClient).inspection())

    @overload
    def deferClose(self, arg0: 'AutoCloseable') -> 'AutoCloseable':
        """public <T extends java.lang.AutoCloseable> T dev.ultreon.quantum.client.QuantumClient.deferClose(T)"""
        return 'AutoCloseable'.__wrap(super(__QuantumClient, self).deferClose(arg0))

    @override
    @overload
    def pollAll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.pollAll()"""
        super(util.PollingExecutorService, self).pollAll()

    @overload
    def isFullScreen(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isFullScreen()"""
        return bool.__wrap(super(QuantumClient, self).isFullScreen())

    @overload
    def playSound(self, arg0: 'SoundEvent', arg1: float):
        """public void dev.ultreon.quantum.client.QuantumClient.playSound(dev.ultreon.quantum.world.SoundEvent,float)"""
        super(__QuantumClient, self).playSound(arg0, __float.valueOf(arg1))

    @overload
    def runInTick(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.client.QuantumClient.runInTick(java.lang.Runnable)"""
        super(__QuantumClient, self).runInTick(arg0)

    @property
    def input(self) -> GameInput:
        return GameInput.__wrap(super(__QuantumClient).input())

    @overload
    def pause(self):
        """public void dev.ultreon.quantum.client.QuantumClient.pause()"""
        super(QuantumClient, self).pause()

    @override
    @overload
    def poll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.poll()"""
        super(util.PollingExecutorService, self).poll()

    @overload
    def deferDispose(self, arg0: 'Disposable') -> 'utils.Disposable':
        """public <T extends com.badlogic.gdx.utils.Disposable> T dev.ultreon.quantum.client.QuantumClient.deferDispose(T)"""
        return 'utils.Disposable'.__wrap(super(__QuantumClient, self).deferDispose(arg0))

    @overload
    def reloadResourcesAsync(self):
        """public void dev.ultreon.quantum.client.QuantumClient.reloadResourcesAsync()"""
        super(QuantumClient, self).reloadResourcesAsync()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def showScreen(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.showScreen(dev.ultreon.quantum.client.gui.Screen)"""
        return bool.__wrap(super(__QuantumClient, self).showScreen(arg0))

    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.QuantumClient.getWidth()"""
        return int.__wrap(super(QuantumClient, self).getWidth())

    @property
    def notifications(self) -> NotifyManager:
        return NotifyManager.__wrap(super(__QuantumClient).notifications())

    @staticmethod
    @overload
    def getGameEnv() -> 'GameEnvironment':
        """public static dev.ultreon.quantum.client.GameEnvironment dev.ultreon.quantum.client.QuantumClient.getGameEnv()"""
        return GameEnvironment.__wrap(__QuantumClient.getGameEnv())

    @property
    def clipboard(self) -> IClipboard:
        return IClipboard.__wrap(super(__QuantumClient).clipboard())

    @property
    def worldRenderer(self) -> WorldRenderer:
        return WorldRenderer.__wrap(super(__QuantumClient).worldRenderer())

    @overload
    def screenshot(self, arg0: bool) -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<dev.ultreon.quantum.client.Screenshot> dev.ultreon.quantum.client.QuantumClient.screenshot(boolean)"""
        return 'CompletableFuture'.__wrap(super(__QuantumClient, self).screenshot(__boolean.valueOf(arg0)))

    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.QuantumClient.getHeight()"""
        return int.__wrap(super(QuantumClient, self).getHeight())

    @overload
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__util.PollingExecutorService, self).invokeAny(arg0, __long.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def getGameDir() -> 'Path':
        """public static java.nio.file.Path dev.ultreon.quantum.client.QuantumClient.getGameDir()"""
        return Path.__wrap(__QuantumClient.getGameDir())

    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.QuantumClient.resize(int,int)"""
        super(__QuantumClient, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getPipeline(self) -> 'pipeline.RenderPipeline':
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline dev.ultreon.quantum.client.QuantumClient.getPipeline()"""
        return 'pipeline.RenderPipeline'.__wrap(super(QuantumClient, self).getPipeline())

    @overload
    def isShowingImGui(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isShowingImGui()"""
        return bool.__wrap(super(QuantumClient, self).isShowingImGui())

    @property
    def newFont(self) -> Font:
        return Font.__wrap(super(__QuantumClient).newFont())

    @overload
    def getScaledHeight(self) -> int:
        """public int dev.ultreon.quantum.client.QuantumClient.getScaledHeight()"""
        return int.__wrap(super(QuantumClient, self).getScaledHeight())

    @overload
    def getModConfigScreen(self, arg0: 'Mod') -> 'config.ConfigScreenFactory':
        """public dev.ultreon.quantum.client.config.ConfigScreenFactory dev.ultreon.quantum.client.QuantumClient.getModConfigScreen(dev.ultreon.quantum.Mod)"""
        return 'config.ConfigScreenFactory'.__wrap(super(__QuantumClient, self).getModConfigScreen(arg0))

    @overload
    def schedule(self, arg0: 'Task', arg1: int, arg2: 'TimeUnit') -> 'ScheduledFuture':
        """public java.util.concurrent.ScheduledFuture<java.lang.Void> dev.ultreon.quantum.client.QuantumClient.schedule(dev.ultreon.quantum.util.Task<?>,long,java.util.concurrent.TimeUnit)"""
        return 'ScheduledFuture'.__wrap(super(__QuantumClient, self).schedule(arg0, __long.valueOf(arg1), arg2))

    @overload
    def isInThirdPerson(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isInThirdPerson()"""
        return bool.__wrap(super(QuantumClient, self).isInThirdPerson())

    @property
    def serverData(self, value: 'ServerData'):
        super(__QuantumClient).serverData(value)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @property
    def playerInput(self) -> PlayerInput:
        return PlayerInput.__wrap(super(__QuantumClient).playerInput())

    @overload
    def setShowDebugHud(self, arg0: bool):
        """public void dev.ultreon.quantum.client.QuantumClient.setShowDebugHud(boolean)"""
        super(__QuantumClient, self).setShowDebugHud(__boolean.valueOf(arg0))

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isShutdown()"""
        return bool.__wrap(super(util.PollingExecutorService, self).isShutdown())

    @property
    def settings(self) -> GameSettings:
        return GameSettings.__wrap(super(__QuantumClient).settings())

    @overload
    def delayDispose(self, arg0: 'Disposable'):
        """public void dev.ultreon.quantum.client.QuantumClient.delayDispose(com.badlogic.gdx.utils.Disposable)"""
        super(__QuantumClient, self).delayDispose(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @property
    def integratedServer(self) -> IntegratedServer:
        return IntegratedServer.__wrap(super(__QuantumClient).integratedServer())

    @overload
    def pollServerTick(self):
        """public void dev.ultreon.quantum.client.QuantumClient.pollServerTick()"""
        super(QuantumClient, self).pollServerTick()

    @staticmethod
    @overload
    def isOnMainThread() -> bool:
        """public static boolean dev.ultreon.quantum.client.QuantumClient.isOnMainThread()"""
        return bool.__wrap(__QuantumClient.isOnMainThread())

    @property
    def emmisiveTextureAtlas(self, value: 'atlas.TextureAtlas'):
        super(__QuantumClient).emmisiveTextureAtlas(value)

    @overload
    def startBreaking(self):
        """public void dev.ultreon.quantum.client.QuantumClient.startBreaking()"""
        super(QuantumClient, self).startBreaking()

    @overload
    def invokeAll(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit)"""
        return 'List'.__wrap(super(__util.PollingExecutorService, self).invokeAll(arg0, __long.valueOf(arg1), arg2))

    @property
    def openedWorld(self) -> WorldStorage:
        return WorldStorage.__wrap(super(__QuantumClient).openedWorld())

    @overload
    def schedule(self, arg0: 'Task', arg1: int) -> 'ScheduledFuture':
        """public java.util.concurrent.ScheduledFuture<java.lang.Void> dev.ultreon.quantum.client.QuantumClient.schedule(dev.ultreon.quantum.util.Task<?>,long)"""
        return 'ScheduledFuture'.__wrap(super(__QuantumClient, self).schedule(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def reloadResources(self):
        """public void dev.ultreon.quantum.client.QuantumClient.reloadResources()"""
        super(QuantumClient, self).reloadResources()

    @overload
    def cyclePlayerView(self):
        """public void dev.ultreon.quantum.client.QuantumClient.cyclePlayerView()"""
        super(QuantumClient, self).cyclePlayerView()

    @property
    def world(self) -> ClientWorld:
        return ClientWorld.__wrap(super(__QuantumClient).world())

    @property
    def soundRegistry(self) -> ClientSoundRegistry:
        return ClientSoundRegistry.__wrap(super(__QuantumClient).soundRegistry())

    @staticmethod
    @overload
    def invoke(arg0: 'Callable') -> 'CompletableFuture':
        """public static <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.client.QuantumClient.invoke(java.util.concurrent.Callable<T>)"""
        return CompletableFuture.__wrap(__QuantumClient.invoke(arg0))

    @property
    def debugGui(self) -> DebugOverlay:
        return DebugOverlay.__wrap(super(__QuantumClient).debugGui())

    @property
    def motionPointer(self) -> TouchPoint:
        return TouchPoint.__wrap(super(__QuantumClient).motionPointer())

    @property
    def profiler(self) -> Profiler:
        return Profiler.__wrap(super(__PollingExecutorService).profiler())

    @property
    def cursor(self, value: 'util.BlockHitResult'):
        super(__QuantumClient).cursor(value)

    @staticmethod
    @overload
    def ggBro() -> 'util.GG':
        """public static dev.ultreon.quantum.client.util.GG dev.ultreon.quantum.client.QuantumClient.ggBro()"""
        return util.GG.__wrap(__QuantumClient.ggBro())

    @overload
    def setInThirdPerson(self, arg0: bool):
        """public void dev.ultreon.quantum.client.QuantumClient.setInThirdPerson(boolean)"""
        super(__QuantumClient, self).setInThirdPerson(__boolean.valueOf(arg0))

    @overload
    def setShowingImGui(self, arg0: bool):
        """public void dev.ultreon.quantum.client.QuantumClient.setShowingImGui(boolean)"""
        super(__QuantumClient, self).setShowingImGui(__boolean.valueOf(arg0))

    @overload
    def isShowDebugHud(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isShowDebugHud()"""
        return bool.__wrap(super(QuantumClient, self).isShowDebugHud())

    @overload
    def getBlockModel(self, arg0: 'BlockProperties') -> 'block.BlockModel':
        """public dev.ultreon.quantum.client.model.block.BlockModel dev.ultreon.quantum.client.QuantumClient.getBlockModel(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'block.BlockModel'.__wrap(super(__QuantumClient, self).getBlockModel(arg0))

    @overload
    def getShaderProviderManager(self) -> 'management.ShaderProviderManager':
        """public dev.ultreon.quantum.client.management.ShaderProviderManager dev.ultreon.quantum.client.QuantumClient.getShaderProviderManager()"""
        return 'management.ShaderProviderManager'.__wrap(super(QuantumClient, self).getShaderProviderManager())

    @overload
    def setAutomaticScale(self, arg0: bool):
        """public void dev.ultreon.quantum.client.QuantumClient.setAutomaticScale(boolean)"""
        super(__QuantumClient, self).setAutomaticScale(__boolean.valueOf(arg0))

    @overload
    def exitWorldToTitle(self):
        """public void dev.ultreon.quantum.client.QuantumClient.exitWorldToTitle()"""
        super(QuantumClient, self).exitWorldToTitle()

    @overload
    def deferShutdown(self, arg0: 'Shutdownable') -> 'util.Shutdownable':
        """public <T extends dev.ultreon.quantum.util.Shutdownable> T dev.ultreon.quantum.client.QuantumClient.deferShutdown(T)"""
        return 'util.Shutdownable'.__wrap(super(__QuantumClient, self).deferShutdown(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @property
    def emmisiveTextureAtlas(self) -> TextureAtlas:
        return TextureAtlas.__wrap(super(__QuantumClient).emmisiveTextureAtlas())

    @overload
    def exitWorldAndThen(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.client.QuantumClient.exitWorldAndThen(java.lang.Runnable)"""
        super(__QuantumClient, self).exitWorldAndThen(arg0)

    @staticmethod
    @overload
    def getIcons() -> List[str]:
        """public static java.lang.String[] dev.ultreon.quantum.client.QuantumClient.getIcons()"""
        return List[str].__wrap(__QuantumClient.getIcons())

    @property
    def metadata(self) -> Metadata:
        return Metadata.__wrap(super(__QuantumClient).metadata())

    @overload
    def invokeAll(self, arg0: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>)"""
        return 'List'.__wrap(super(__util.PollingExecutorService, self).invokeAll(arg0))

    @property
    def hud(self) -> Hud:
        return Hud.__wrap(super(__QuantumClient).hud())

    @overload
    def getSingleplayerServer(self) -> 'IntegratedServer':
        """public dev.ultreon.quantum.client.IntegratedServer dev.ultreon.quantum.client.QuantumClient.getSingleplayerServer()"""
        return 'IntegratedServer'.__wrap(super(QuantumClient, self).getSingleplayerServer())

    @staticmethod
    @overload
    def crash(arg0: 'CrashLog'):
        """public static void dev.ultreon.quantum.client.QuantumClient.crash(dev.ultreon.quantum.crash.CrashLog)"""
        __QuantumClient.crash(arg0)

    @overload
    def render(self):
        """public void dev.ultreon.quantum.client.QuantumClient.render()"""
        super(QuantumClient, self).render()

    @overload
    def clientTick(self):
        """public void dev.ultreon.quantum.client.QuantumClient.clientTick()"""
        super(QuantumClient, self).clientTick()

    @overload
    def fillGameInfo(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.client.QuantumClient.fillGameInfo(dev.ultreon.quantum.crash.CrashLog)"""
        super(__QuantumClient, self).fillGameInfo(arg0)

    @overload
    def getGuiScale(self) -> float:
        """public float dev.ultreon.quantum.client.QuantumClient.getGuiScale()"""
        return float.__wrap(super(QuantumClient, self).getGuiScale())

    @property
    def input(self, value: 'input.GameInput'):
        super(__QuantumClient).input(value)

    @property
    def connection(self, value: 'system.IConnection'):
        super(__QuantumClient).connection(value)

    @staticmethod
    @overload
    def setCrashHook(arg0: 'Callback'):
        """public static void dev.ultreon.quantum.client.QuantumClient.setCrashHook(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.crash.CrashLog>)"""
        __QuantumClient.setCrashHook(arg0)

    @property
    def itemTextureAtlas(self) -> TextureAtlas:
        return TextureAtlas.__wrap(super(__QuantumClient).itemTextureAtlas())

    @property
    def debugGui(self, value: 'debug.DebugOverlay'):
        super(__QuantumClient).debugGui(value)

    @staticmethod
    @overload
    def invoke(arg0: 'Runnable') -> 'CompletableFuture':
        """public static java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.client.QuantumClient.invoke(java.lang.Runnable)"""
        return CompletableFuture.__wrap(__QuantumClient.invoke(arg0))

    @overload
    def getTextureManager(self) -> 'texture.TextureManager':
        """public dev.ultreon.quantum.client.texture.TextureManager dev.ultreon.quantum.client.QuantumClient.getTextureManager()"""
        return 'texture.TextureManager'.__wrap(super(QuantumClient, self).getTextureManager())

    @overload
    def isClosingWorld(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isClosingWorld()"""
        return bool.__wrap(super(QuantumClient, self).isClosingWorld())

    @overload
    def submit(self, arg0: 'Runnable', arg1: object) -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable,T)"""
        return 'CompletableFuture'.__wrap(super(__util.PollingExecutorService, self).submit(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def close(self):
        """public default void java.util.concurrent.ExecutorService.close()"""
        super(ExecutorService, self).close()

    @staticmethod
    @overload
    def id(arg0: str) -> 'util.Identifier':
        """public static dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.QuantumClient.id(java.lang.String)"""
        return util.Identifier.__wrap(__QuantumClient.id(arg0))

    @property
    def blocksTextureAtlas(self) -> TextureAtlas:
        return TextureAtlas.__wrap(super(__QuantumClient).blocksTextureAtlas())

    @staticmethod
    @overload
    def strId(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.quantum.client.QuantumClient.strId(java.lang.String)"""
        return str.__wrap(__QuantumClient.strId(arg0))

    @overload
    def resetBreaking(self):
        """public void dev.ultreon.quantum.client.QuantumClient.resetBreaking()"""
        super(QuantumClient, self).resetBreaking()

    @property
    def entityRendererManager(self) -> EntityRendererRegistry:
        return EntityRendererRegistry.__wrap(super(__QuantumClient).entityRendererManager())

    @overload
    def addFuture(self, arg0: 'CompletableFuture'):
        """public void dev.ultreon.quantum.client.QuantumClient.addFuture(java.util.concurrent.CompletableFuture<?>)"""
        super(__QuantumClient, self).addFuture(arg0)

    @property
    def screen(self) -> Screen:
        return Screen.__wrap(super(__QuantumClient).screen())

    @staticmethod
    @overload
    def data(arg0: str) -> 'files.FileHandle':
        """public static com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.QuantumClient.data(java.lang.String)"""
        return files.FileHandle.__wrap(__QuantumClient.data(arg0))

    @property
    def inspection(self, value: 'inspect.InspectionRoot'):
        super(__QuantumClient).inspection(value)

    @overload
    def getEnvironment(self) -> 'g3d.Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment dev.ultreon.quantum.client.QuantumClient.getEnvironment()"""
        return 'g3d.Environment'.__wrap(super(QuantumClient, self).getEnvironment())

    @property
    def newConfig(self) -> ClientConfig:
        return ClientConfig.__wrap(super(__QuantumClient).newConfig())

    @overload
    def onDisconnect(self, arg0: str):
        """public void dev.ultreon.quantum.client.QuantumClient.onDisconnect(java.lang.String)"""
        super(__QuantumClient, self).onDisconnect(arg0)

    @overload
    def setGuiScale(self, arg0: float):
        """public void dev.ultreon.quantum.client.QuantumClient.setGuiScale(float)"""
        super(__QuantumClient, self).setGuiScale(__float.valueOf(arg0))

    @property
    def blocksTextureAtlas(self, value: 'atlas.TextureAtlas'):
        super(__QuantumClient).blocksTextureAtlas(value)

    @overload
    def getMultiplayerData(self) -> 'multiplayer.MultiplayerData':
        """public dev.ultreon.quantum.client.multiplayer.MultiplayerData dev.ultreon.quantum.client.QuantumClient.getMultiplayerData()"""
        return 'multiplayer.MultiplayerData'.__wrap(super(QuantumClient, self).getMultiplayerData())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.QuantumClient.dispose()"""
        super(QuantumClient, self).dispose()

    @property
    def motionPointer(self, value: 'input.TouchPoint'):
        super(__QuantumClient).motionPointer(value)

    @overload
    def getPlayerView(self) -> 'util.PlayerView':
        """public dev.ultreon.quantum.client.util.PlayerView dev.ultreon.quantum.client.QuantumClient.getPlayerView()"""
        return 'util.PlayerView'.__wrap(super(QuantumClient, self).getPlayerView())

    @overload
    def isSinglePlayer(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isSinglePlayer()"""
        return bool.__wrap(super(QuantumClient, self).isSinglePlayer())

    @property
    def itemRenderer(self) -> ItemRenderer:
        return ItemRenderer.__wrap(super(__QuantumClient).itemRenderer())

    @property
    def cursor(self) -> BlockHitResult:
        return BlockHitResult.__wrap(super(__QuantumClient).cursor())

    @staticmethod
    @overload
    def interpolate(arg0: float, arg1: float, arg2: float) -> float:
        """public static double dev.ultreon.quantum.client.QuantumClient.interpolate(double,double,double)"""
        return float.__wrap(__QuantumClient.interpolate(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def setPlayerView(self, arg0: 'PlayerView'):
        """public void dev.ultreon.quantum.client.QuantumClient.setPlayerView(dev.ultreon.quantum.client.util.PlayerView)"""
        super(__QuantumClient, self).setPlayerView(arg0)

    @staticmethod
    @overload
    def get() -> 'QuantumClient':
        """public static dev.ultreon.quantum.client.QuantumClient dev.ultreon.quantum.client.QuantumClient.get()"""
        return QuantumClient.__wrap(__QuantumClient.get())

    @staticmethod
    @overload
    def setFpsLimit(arg0: int):
        """public static void dev.ultreon.quantum.client.QuantumClient.setFpsLimit(int)"""
        __QuantumClient.setFpsLimit(__int.valueOf(arg0))

    @property
    def camera(self) -> GameCamera:
        return GameCamera.__wrap(super(__QuantumClient).camera())

    @staticmethod
    @overload
    def resource(arg0: 'Identifier') -> 'files.FileHandle':
        """public static com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.QuantumClient.resource(dev.ultreon.quantum.util.Identifier)"""
        return files.FileHandle.__wrap(__QuantumClient.resource(arg0))

    @overload
    def isPlaying(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isPlaying()"""
        return bool.__wrap(super(QuantumClient, self).isPlaying())

    @overload
    def invokeAny(self, arg0: 'Collection') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__util.PollingExecutorService, self).invokeAny(arg0))

    @overload
    def getWindow(self) -> 'pyquantum.GameWindow':
        """public dev.ultreon.quantum.GameWindow dev.ultreon.quantum.client.QuantumClient.getWindow()"""
        return 'pyquantum.GameWindow'.__wrap(super(QuantumClient, self).getWindow())

    @overload
    def setFullScreen(self, arg0: bool):
        """public void dev.ultreon.quantum.client.QuantumClient.setFullScreen(boolean)"""
        super(__QuantumClient, self).setFullScreen(__boolean.valueOf(arg0))

    @overload
    def setModConfigScreen(self, arg0: 'Mod', arg1: 'ConfigScreenFactory'):
        """public void dev.ultreon.quantum.client.QuantumClient.setModConfigScreen(dev.ultreon.quantum.Mod,dev.ultreon.quantum.client.config.ConfigScreenFactory)"""
        super(__QuantumClient, self).setModConfigScreen(arg0, arg1)

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Callable') -> object:
        """public static <T> T dev.ultreon.quantum.client.QuantumClient.invokeAndWait(java.util.concurrent.Callable<T>)"""
        return object.__wrap(__QuantumClient.invokeAndWait(arg0))

    @overload
    def getShaderProgramManager(self) -> 'management.ShaderProgramManager':
        """public dev.ultreon.quantum.client.management.ShaderProgramManager dev.ultreon.quantum.client.QuantumClient.getShaderProgramManager()"""
        return 'management.ShaderProgramManager'.__wrap(super(QuantumClient, self).getShaderProgramManager())

    @overload
    def resume(self):
        """public void dev.ultreon.quantum.client.QuantumClient.resume()"""
        super(QuantumClient, self).resume()

    @property
    def font(self) -> Font:
        return Font.__wrap(super(__QuantumClient).font())

    @staticmethod
    @overload
    def getGameVersion() -> str:
        """public static java.lang.String dev.ultreon.quantum.client.QuantumClient.getGameVersion()"""
        return str.__wrap(__QuantumClient.getGameVersion())

    @overload
    def getAssetManager(self) -> 'assets.AssetManager':
        """public com.badlogic.gdx.assets.AssetManager dev.ultreon.quantum.client.QuantumClient.getAssetManager()"""
        return 'assets.AssetManager'.__wrap(super(QuantumClient, self).getAssetManager())

    @overload
    def submit(self, arg0: 'Runnable') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable)"""
        return 'CompletableFuture'.__wrap(super(__util.PollingExecutorService, self).submit(arg0))

    @overload
    def isDevMode(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isDevMode()"""
        return bool.__wrap(super(QuantumClient, self).isDevMode())

    @overload
    def getBreakProgress(self) -> float:
        """public float dev.ultreon.quantum.client.QuantumClient.getBreakProgress()"""
        return float.__wrap(super(QuantumClient, self).getBreakProgress())

        @staticmethod
        @overload
        def logDebug():
            """public static void dev.ultreon.quantum.client.QuantumClient.logDebug()"""
            __QuantumClient.logDebug()

    @property
    def hud(self, value: 'gui.Hud'):
        super(__QuantumClient).hud(value)

    @overload
    def startDevWorld(self):
        """public void dev.ultreon.quantum.client.QuantumClient.startDevWorld()"""
        super(QuantumClient, self).startDevWorld()

    @overload
    def delayCrash(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.client.QuantumClient.delayCrash(dev.ultreon.quantum.crash.CrashLog)"""
        super(__QuantumClient, self).delayCrash(arg0)

    @overload
    def playSound(self, arg0: 'ClientSound'):
        """public void dev.ultreon.quantum.client.QuantumClient.playSound(dev.ultreon.quantum.client.audio.ClientSound)"""
        super(__QuantumClient, self).playSound(arg0)

    @property
    def connection(self) -> IConnection:
        return IConnection.__wrap(super(__QuantumClient).connection())

    @property
    def screen(self, value: 'gui.Screen'):
        super(__QuantumClient).screen(value)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.QuantumClient.toString()"""
        return str.__wrap(super(QuantumClient, self).toString())

    @property
    def worldRenderer(self, value: 'world.WorldRenderer'):
        super(__QuantumClient).worldRenderer(value)

    @overload
    def tryShutdown(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.tryShutdown()"""
        return bool.__wrap(super(QuantumClient, self).tryShutdown())

    @overload
    def connectToServer(self, arg0: str, arg1: int):
        """public void dev.ultreon.quantum.client.QuantumClient.connectToServer(java.lang.String,int)"""
        super(__QuantumClient, self).connectToServer(arg0, __int.valueOf(arg1))

    @overload
    def isLoading(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isLoading()"""
        return bool.__wrap(super(QuantumClient, self).isLoading())

    @property
    def player(self, value: 'player.LocalPlayer'):
        super(__QuantumClient).player(value)

    @overload
    def submit(self, arg0: 'Callable') -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'CompletableFuture'.__wrap(super(__util.PollingExecutorService, self).submit(arg0))

    @override
    @overload
    def isTerminated(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isTerminated()"""
        return bool.__wrap(super(util.PollingExecutorService, self).isTerminated())

    @overload
    def getSkinManager(self) -> 'player.SkinManager':
        """public dev.ultreon.quantum.client.player.SkinManager dev.ultreon.quantum.client.QuantumClient.getSkinManager()"""
        return 'player.SkinManager'.__wrap(super(QuantumClient, self).getSkinManager())

    @property
    def world(self, value: 'world.ClientWorld'):
        super(__QuantumClient).world(value)

    @property
    def settings(self, value: 'config.GameSettings'):
        super(__QuantumClient).settings(value)

    @property
    def openedWorld(self, value: 'world.WorldStorage'):
        super(__QuantumClient).openedWorld(value)

    @property
    def entityModelManager(self) -> EntityModelRegistry:
        return EntityModelRegistry.__wrap(super(__QuantumClient).entityModelManager())

    @overload
    def stopBreaking(self):
        """public void dev.ultreon.quantum.client.QuantumClient.stopBreaking()"""
        super(QuantumClient, self).stopBreaking()

    @property
    def hitResult(self, value: 'util.HitResult'):
        super(__QuantumClient).hitResult(value)

    @overload
    def isCustomBorderShown(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isCustomBorderShown()"""
        return bool.__wrap(super(QuantumClient, self).isCustomBorderShown())

    @overload
    def screenshot(self) -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<dev.ultreon.quantum.client.Screenshot> dev.ultreon.quantum.client.QuantumClient.screenshot()"""
        return 'CompletableFuture'.__wrap(super(QuantumClient, self).screenshot())

    @overload
    def getMaterialManager(self) -> 'management.MaterialManager':
        """public dev.ultreon.quantum.client.management.MaterialManager dev.ultreon.quantum.client.QuantumClient.getMaterialManager()"""
        return 'management.MaterialManager'.__wrap(super(QuantumClient, self).getMaterialManager())

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> dev.ultreon.quantum.util.PollingExecutorService.shutdownNow()"""
        return 'List'.__wrap(super(util.PollingExecutorService, self).shutdownNow())

    @property
    def hitResult(self) -> HitResult:
        return HitResult.__wrap(super(__QuantumClient).hitResult())

    @property
    def newConfig(self, value: 'config.ClientConfig'):
        super(__QuantumClient).newConfig(value)

    @overload
    def isRenderingWorld(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isRenderingWorld()"""
        return bool.__wrap(super(QuantumClient, self).isRenderingWorld())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @property
    def metadata(self, value: 'Metadata'):
        super(__QuantumClient).metadata(value)

    @overload
    def getScaledWidth(self) -> int:
        """public int dev.ultreon.quantum.client.QuantumClient.getScaledWidth()"""
        return int.__wrap(super(QuantumClient, self).getScaledWidth())

    @overload
    def setActivity(self, arg0: 'GameActivity'):
        """public void dev.ultreon.quantum.client.QuantumClient.setActivity(dev.ultreon.quantum.client.rpc.GameActivity)"""
        super(__QuantumClient, self).setActivity(arg0)

    @overload
    def getUser(self) -> 'User':
        """public dev.ultreon.quantum.client.User dev.ultreon.quantum.client.QuantumClient.getUser()"""
        return 'User'.__wrap(super(QuantumClient, self).getUser())

    @property
    def itemTextureAtlas(self, value: 'atlas.TextureAtlas'):
        super(__QuantumClient).itemTextureAtlas(value)

    @overload
    def attack(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.client.QuantumClient.attack(dev.ultreon.quantum.entity.Entity)"""
        super(__QuantumClient, self).attack(arg0)

    @overload
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit') -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__util.PollingExecutorService, self).awaitTermination(__long.valueOf(arg0), arg1))

    @overload
    def startWorld(self, arg0: 'WorldStorage'):
        """public void dev.ultreon.quantum.client.QuantumClient.startWorld(dev.ultreon.quantum.world.WorldStorage)"""
        super(__QuantumClient, self).startWorld(arg0)

    @overload
    def filesDropped(self, arg0: 'String') -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.filesDropped(java.lang.String[])"""
        return bool.__wrap(super(__QuantumClient, self).filesDropped(arg0))

    @overload
    def getCurrentTps(self) -> int:
        """public int dev.ultreon.quantum.client.QuantumClient.getCurrentTps()"""
        return int.__wrap(super(QuantumClient, self).getCurrentTps())

    @staticmethod
    @overload
    def crash(arg0: 'Throwable'):
        """public static void dev.ultreon.quantum.client.QuantumClient.crash(java.lang.Throwable)"""
        __QuantumClient.crash(arg0)

    @property
    def itemRenderer(self, value: 'item.ItemRenderer'):
        super(__QuantumClient).itemRenderer(value)

    @overload
    def getBootTime(self) -> 'v0.Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.quantum.client.QuantumClient.getBootTime()"""
        return 'v0.Duration'.__wrap(super(QuantumClient, self).getBootTime())

    @overload
    def getDrawOffset(self) -> 'math.GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 dev.ultreon.quantum.client.QuantumClient.getDrawOffset()"""
        return 'math.GridPoint2'.__wrap(super(QuantumClient, self).getDrawOffset()) 
 
 
# CLASS: dev.ultreon.quantum.client.Constants
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.Constants as __Constants
__Constants = __Constants
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Constants():
    """dev.ultreon.quantum.client.Constants"""
 
    @staticmethod
    def __wrap(java_value: __Constants) -> 'Constants':
        return Constants(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Constants):
        """
        Dynamic initializer for Constants.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.Constants()"""
        val = __Constants()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.Constants()"""
        val = __Constants()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.client.RenderingRegistration
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.RenderingRegistration as __RenderingRegistration
__RenderingRegistration = __RenderingRegistration
try:
    from pyquantum.client import registry
except ImportError:
    registry = __import_once__("pyquantum.client.registry")

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
 
class RenderingRegistration():
    """dev.ultreon.quantum.client.RenderingRegistration"""
 
    @staticmethod
    def __wrap(java_value: __RenderingRegistration) -> 'RenderingRegistration':
        return RenderingRegistration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderingRegistration):
        """
        Dynamic initializer for RenderingRegistration.
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
    def registerEntityRendering(arg0: 'EntityModelRegistry'):
        """public static void dev.ultreon.quantum.client.RenderingRegistration.registerEntityRendering(dev.ultreon.quantum.client.registry.EntityModelRegistry)"""
        __RenderingRegistration.registerEntityRendering(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def registerRendering(arg0: 'QuantumClient'):
        """public static void dev.ultreon.quantum.client.RenderingRegistration.registerRendering(dev.ultreon.quantum.client.QuantumClient)"""
        __RenderingRegistration.registerRendering(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.RenderingRegistration()"""
        val = __RenderingRegistration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

        @staticmethod
        @overload
        def registerEntityRenderers():
            """public static void dev.ultreon.quantum.client.RenderingRegistration.registerEntityRenderers()"""
            __RenderingRegistration.registerEntityRenderers()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.RenderingRegistration()"""
        val = __RenderingRegistration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))