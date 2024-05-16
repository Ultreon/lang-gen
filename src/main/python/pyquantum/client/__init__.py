from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = _import_once("pyquantum.registry")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.ClientRegistries as _ClientRegistries
_ClientRegistries = _ClientRegistries
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientRegistries():
    """dev.ultreon.quantum.client.ClientRegistries"""
 
    @staticmethod
    def _wrap(java_value: _ClientRegistries) -> 'ClientRegistries':
        return ClientRegistries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientRegistries):
        """
        Dynamic initializer for ClientRegistries.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientRegistries__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientRegistries__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.gui.debug.DebugPage> dev.ultreon.quantum.client.ClientRegistries.DEBUG_PAGE
    DEBUG_PAGE: 'registry.Registry' = _wrap(_registry.Registry.DEBUG_PAGE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.render.RenderLayer> dev.ultreon.quantum.client.ClientRegistries.RENDER_LAYER
    RENDER_LAYER: 'registry.Registry' = _wrap(_registry.Registry.RENDER_LAYER)

    # public static final dev.ultreon.quantum.registry.Registry<com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter> dev.ultreon.quantum.client.ClientRegistries.PARTICLE_EMITTER
    PARTICLE_EMITTER: 'registry.Registry' = _wrap(_registry.Registry.PARTICLE_EMITTER)

    # public static final dev.ultreon.quantum.registry.Registry<com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer<?, ?>> dev.ultreon.quantum.client.ClientRegistries.PARTICLE_CONTROLLER_RENDERER
    PARTICLE_CONTROLLER_RENDERER: 'registry.Registry' = _wrap(_registry.Registry.PARTICLE_CONTROLLER_RENDERER)

    # public static final dev.ultreon.quantum.registry.Registry<com.badlogic.gdx.graphics.g3d.particles.ParticleController> dev.ultreon.quantum.client.ClientRegistries.PARTICLE_CONTROLLER
    PARTICLE_CONTROLLER: 'registry.Registry' = _wrap(_registry.Registry.PARTICLE_CONTROLLER)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.font.Font> dev.ultreon.quantum.client.ClientRegistries.FONT
    FONT: 'registry.Registry' = _wrap(_registry.Registry.FONT)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.ClientRegistries()"""
        val = _ClientRegistries()
        self.__wrapper = val

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.ClientRegistries()"""
        val = _ClientRegistries()
        self.__wrapper = val

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

 
 
 
# CLASS: dev.ultreon.quantum.client.ClientRegistries
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = _import_once("pyquantum.registry")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.ClientRegistries as _ClientRegistries
_ClientRegistries = _ClientRegistries
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientRegistries():
    """dev.ultreon.quantum.client.ClientRegistries"""
 
    @staticmethod
    def _wrap(java_value: _ClientRegistries) -> 'ClientRegistries':
        return ClientRegistries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientRegistries):
        """
        Dynamic initializer for ClientRegistries.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientRegistries__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientRegistries__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.gui.debug.DebugPage> dev.ultreon.quantum.client.ClientRegistries.DEBUG_PAGE
    DEBUG_PAGE: 'registry.Registry' = _wrap(_registry.Registry.DEBUG_PAGE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.render.RenderLayer> dev.ultreon.quantum.client.ClientRegistries.RENDER_LAYER
    RENDER_LAYER: 'registry.Registry' = _wrap(_registry.Registry.RENDER_LAYER)

    # public static final dev.ultreon.quantum.registry.Registry<com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter> dev.ultreon.quantum.client.ClientRegistries.PARTICLE_EMITTER
    PARTICLE_EMITTER: 'registry.Registry' = _wrap(_registry.Registry.PARTICLE_EMITTER)

    # public static final dev.ultreon.quantum.registry.Registry<com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer<?, ?>> dev.ultreon.quantum.client.ClientRegistries.PARTICLE_CONTROLLER_RENDERER
    PARTICLE_CONTROLLER_RENDERER: 'registry.Registry' = _wrap(_registry.Registry.PARTICLE_CONTROLLER_RENDERER)

    # public static final dev.ultreon.quantum.registry.Registry<com.badlogic.gdx.graphics.g3d.particles.ParticleController> dev.ultreon.quantum.client.ClientRegistries.PARTICLE_CONTROLLER
    PARTICLE_CONTROLLER: 'registry.Registry' = _wrap(_registry.Registry.PARTICLE_CONTROLLER)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.font.Font> dev.ultreon.quantum.client.ClientRegistries.FONT
    FONT: 'registry.Registry' = _wrap(_registry.Registry.FONT)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.ClientRegistries()"""
        val = _ClientRegistries()
        self.__wrapper = val

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.ClientRegistries()"""
        val = _ClientRegistries()
        self.__wrapper = val

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

 
 
 
# CLASS: dev.ultreon.quantum.client.ClientRegistries 
 
 
# CLASS: dev.ultreon.quantum.client.ServerData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.client.ServerData as _ServerData
_ServerData = _ServerData
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ServerData():
    """dev.ultreon.quantum.client.ServerData"""
 
    @staticmethod
    def _wrap(java_value: _ServerData) -> 'ServerData':
        return ServerData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerData):
        """
        Dynamic initializer for ServerData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerData__wrapper":
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.ServerData.toString()"""
        return str._wrap(super(ServerData, self).toString())

    @overload
    def address(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.ServerData.address()"""
        return str._wrap(super(ServerData, self).address())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.ServerData.hashCode()"""
        return int._wrap(super(ServerData, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.ServerData.equals(java.lang.Object)"""
        return bool._wrap(super(_ServerData, self).equals(arg0))

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.ServerData.name()"""
        return str._wrap(super(ServerData, self).name())

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.client.ServerData(java.lang.String,java.lang.String)"""
        val = _ServerData(arg0, arg1)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.GameLibGDXWrapper
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.GameLibGDXWrapper as _GameLibGDXWrapper
_GameLibGDXWrapper = _GameLibGDXWrapper
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GameLibGDXWrapper():
    """dev.ultreon.quantum.client.GameLibGDXWrapper"""
 
    @staticmethod
    def _wrap(java_value: _GameLibGDXWrapper) -> 'GameLibGDXWrapper':
        return GameLibGDXWrapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GameLibGDXWrapper):
        """
        Dynamic initializer for GameLibGDXWrapper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GameLibGDXWrapper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GameLibGDXWrapper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def resume(self):
        """public void dev.ultreon.quantum.client.GameLibGDXWrapper.resume()"""
        super(GameLibGDXWrapper, self).resume()

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
    def render(self):
        """public void dev.ultreon.quantum.client.GameLibGDXWrapper.render()"""
        super(GameLibGDXWrapper, self).render()

    @override
    @overload
    def create(self):
        """public void dev.ultreon.quantum.client.GameLibGDXWrapper.create()"""
        super(GameLibGDXWrapper, self).create()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.GameLibGDXWrapper.dispose()"""
        super(GameLibGDXWrapper, self).dispose()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.GameLibGDXWrapper.resize(int,int)"""
        super(_GameLibGDXWrapper, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createInstance(arg0: 'String') -> 'GameLibGDXWrapper':
        """public static dev.ultreon.quantum.client.GameLibGDXWrapper dev.ultreon.quantum.client.GameLibGDXWrapper.createInstance(java.lang.String[])"""
        return GameLibGDXWrapper._wrap(_GameLibGDXWrapper.createInstance(arg0))

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

    @override
    @overload
    def pause(self):
        """public void dev.ultreon.quantum.client.GameLibGDXWrapper.pause()"""
        super(GameLibGDXWrapper, self).pause()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.ClientResources
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import com.badlogic.gdx.graphics.g2d.BitmapFont as _BitmapFont
_BitmapFont = _BitmapFont
import java.lang.Integer as _int
import dev.ultreon.quantum.client.ClientResources as _ClientResources
_ClientResources = _ClientResources
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientResources():
    """dev.ultreon.quantum.client.ClientResources"""
 
    @staticmethod
    def _wrap(java_value: _ClientResources) -> 'ClientResources':
        return ClientResources(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientResources):
        """
        Dynamic initializer for ClientResources.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientResources__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientResources__wrapper":
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
    def bitmapFont(arg0: 'Identifier') -> 'g2d.BitmapFont':
        """public static com.badlogic.gdx.graphics.g2d.BitmapFont dev.ultreon.quantum.client.ClientResources.bitmapFont(dev.ultreon.quantum.util.Identifier)"""
        return g2d.BitmapFont._wrap(_ClientResources.bitmapFont(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.ClientResources()"""
        val = _ClientResources()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.ClientResources()"""
        val = _ClientResources()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.client.GameClipboard
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.awt.datatransfer.Clipboard as Clipboard
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.awt.image.BufferedImage as BufferedImage
import dev.ultreon.quantum.client.GameClipboard as _GameClipboard
_GameClipboard = _GameClipboard
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GameClipboard():
    """dev.ultreon.quantum.client.GameClipboard"""
 
    @staticmethod
    def _wrap(java_value: _GameClipboard) -> 'GameClipboard':
        return GameClipboard(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GameClipboard):
        """
        Dynamic initializer for GameClipboard.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GameClipboard__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GameClipboard__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def paste(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.GameClipboard.paste()"""
        return str._wrap(super(GameClipboard, self).paste())

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
    def copy(self, arg0: str):
        """public void dev.ultreon.quantum.client.GameClipboard.copy(java.lang.String)"""
        super(_GameClipboard, self).copy(arg0)

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
    def __init__(self, arg0: 'Clipboard'):
        """public dev.ultreon.quantum.client.GameClipboard(java.awt.datatransfer.Clipboard)"""
        val = _GameClipboard(arg0)
        self.__wrapper = val

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

    @override
    @overload
    def copy(self, arg0: 'BufferedImage'):
        """public void dev.ultreon.quantum.client.GameClipboard.copy(java.awt.image.BufferedImage)"""
        super(_GameClipboard, self).copy(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.DevScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.UIContainer as _UIContainer
_UIContainer = _UIContainer
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.gui.widget.layout.Layout as _Layout
_Layout = _Layout
import dev.ultreon.quantum.client.gui.Screen as _Screen
_Screen = _Screen
try:
    from pyquantum import component
except ImportError:
    component = _import_once("pyquantum.component")

import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = _import_once("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.client.gui.Dialog as _Dialog
_Dialog = _Dialog
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.client.DevScreen as _DevScreen
_DevScreen = _DevScreen
import dev.ultreon.quantum.client.gui.widget.Widget as _Widget
_Widget = _Widget
import dev.ultreon.quantum.client.gui.Position as _Position
_Position = _Position
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DevScreen():
    """dev.ultreon.quantum.client.DevScreen"""
 
    @staticmethod
    def _wrap(java_value: _DevScreen) -> 'DevScreen':
        return DevScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DevScreen):
        """
        Dynamic initializer for DevScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DevScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DevScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(_gui.Screen, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'._wrap(super(gui.Screen, self).getTitle())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_widget.Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_widget.Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.DevScreen.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_DevScreen, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_widget.Widget, self).setPos(arg0)

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'._wrap(super(_widget.UIContainer, self).getWidgetsAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(widget.Widget, self).getX())

    @overload
    def title(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).title(arg0))

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_widget.Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(widget.Widget, self).isFocused())

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_widget.Widget, self).onRevalidate(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(widget.Widget, self).isEnabled())

    @override
    @overload
    def getDialog(self) -> 'gui.Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'gui.Dialog'._wrap(super(gui.Screen, self).getDialog())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_widget.Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(_gui.Screen, self).closeDialog(arg0)

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'._wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str._wrap(super(gui.Screen, self).getRawTitle())

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool._wrap(super(_gui.Screen, self).onClose(arg0))

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_widget.UIContainer, self).renderChild(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_widget.Widget, self).setSize(arg0)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'._wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str._wrap(super(gui.Screen, self).getName())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool._wrap(_Widget.isPosWithin(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_widget.Widget, self).height(_int.valueOf(arg0))

    @override
    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool._wrap(super(gui.Screen, self).back())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_widget.Widget, self).setEnabled(_boolean.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(widget.Widget, self).isClickable())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(widget.Widget, self).getWidth())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_widget.Widget, self).setBounds(arg0)

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_widget.Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canCloseWithEsc()"""
        return bool._wrap(super(gui.Screen, self).canCloseWithEsc())

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(widget.Widget, self).isHovered())

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(_Screen).parentScreen(value)

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'._wrap(super(gui.Screen, self).path())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_widget.Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_widget.Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(_widget.UIContainer, self).setLayout(arg0)

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(_Screen).directHovered(value)

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(widget.Widget, self).getPreferredHeight())

    @override
    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(_gui.Screen, self).init(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_widget.Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(_gui.Screen, self).showDialog(arg0)

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'._wrap(super(_widget.UIContainer, self).getWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @property
    def focused(self, value: 'widget.Widget'):
        super(_Screen).focused(value)

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool._wrap(super(gui.Screen, self).isHoveringClickable())

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'._wrap(super(_widget.UIContainer, self).position(arg0))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_widget.Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_widget.Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'._wrap(super(widget.UIContainer, self).getLayout())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'._wrap(super(_widget.UIContainer, self).bounds(arg0))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_widget.Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).title(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool._wrap(super(_gui.Screen, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_widget.UIContainer, self).remove(arg0)

    @property
    def focused(self) -> Widget:
        return Widget._wrap(super(_Screen).focused())

    @property
    def directHovered(self) -> Widget:
        return Widget._wrap(super(_Screen).directHovered())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_widget.Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(widget.Widget, self).componentRegistry())

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'._wrap(super(_gui.Screen, self).add(arg0))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_widget.Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool._wrap(super(_gui.Screen, self).filesDropped(arg0))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool._wrap(super(_gui.Screen, self).charType(_char.valueOf(arg0)))

    @property
    def parentScreen(self) -> Screen:
        return Screen._wrap(super(_Screen).parentScreen())

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'._wrap(super(_widget.UIContainer, self).getExactWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.DevScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_DevScreen, self).build(arg0)

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_widget.Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(widget.Widget, self).getPreferredSize())

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canClose()"""
        return bool._wrap(super(gui.Screen, self).canClose())

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.DebugRegistration
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.DebugRegistration as _DebugRegistration
_DebugRegistration = _DebugRegistration
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DebugRegistration():
    """dev.ultreon.quantum.client.DebugRegistration"""
 
    @staticmethod
    def _wrap(java_value: _DebugRegistration) -> 'DebugRegistration':
        return DebugRegistration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DebugRegistration):
        """
        Dynamic initializer for DebugRegistration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DebugRegistration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DebugRegistration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.DebugRegistration()"""
        val = _DebugRegistration()
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.DebugRegistration()"""
        val = _DebugRegistration()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

        @staticmethod
        @overload
        def registerAutoFillers():
            """public static void dev.ultreon.quantum.client.DebugRegistration.registerAutoFillers()"""
            _DebugRegistration.registerAutoFillers()

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
 
 
# CLASS: dev.ultreon.quantum.client.IntegratedServer
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.IntegratedServer as _IntegratedServer
_IntegratedServer = _IntegratedServer
import java.util.UUID as UUID
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

try:
    from pyquantum.client import player
except ImportError:
    player = _import_once("pyquantum.client.player")

try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

try:
    from pyquantum import recipe
except ImportError:
    recipe = _import_once("pyquantum.recipe")

import java.util.Collection as Collection
try:
    from pyquantum import crash
except ImportError:
    crash = _import_once("pyquantum.crash")

import dev.ultreon.quantum.server.player.ServerPlayer as _ServerPlayer
_ServerPlayer = _ServerPlayer
import java.lang.Boolean as _boolean
try:
    from pyquantum.debug import profiler
except ImportError:
    profiler = _import_once("pyquantum.debug.profiler")

import java.util.concurrent.Callable as Callable
import dev.ultreon.quantum.world.WorldStorage as _WorldStorage
_WorldStorage = _WorldStorage
try:
    from pyquantum import gamerule
except ImportError:
    gamerule = _import_once("pyquantum.gamerule")

import dev.ultreon.quantum.server.player.CacheablePlayer as _CacheablePlayer
_CacheablePlayer = _CacheablePlayer
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.world.ServerWorld as _ServerWorld
_ServerWorld = _ServerWorld
import java.lang.Object as _object
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
import java.util.Collection as _Collection
_Collection = _Collection
import java.util.concurrent.TimeUnit as TimeUnit
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.concurrent.CompletableFuture as _CompletableFuture
_CompletableFuture = _CompletableFuture
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

import java.util.concurrent.CompletableFuture as CompletableFuture
import dev.ultreon.quantum.client.QuantumClient as _QuantumClient
_QuantumClient = _QuantumClient
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

import dev.ultreon.quantum.util.PollingExecutorService as _PollingExecutorService
_PollingExecutorService = _PollingExecutorService
import java.util.UUID as _UUID
_UUID = _UUID
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.server.PlayerManager as _PlayerManager
_PlayerManager = _PlayerManager
import java.lang.String as _string
import java.lang.Exception as Exception
import dev.ultreon.quantum.network.Networker as _Networker
_Networker = _Networker
import dev.ultreon.quantum.server.player.PermissionMap as _PermissionMap
_PermissionMap = _PermissionMap
import java.util.concurrent.ScheduledFuture as ScheduledFuture
import dev.ultreon.quantum.debug.profiler.Profiler as _Profiler
_Profiler = _Profiler
import dev.ultreon.quantum.recipe.RecipeManager as _RecipeManager
_RecipeManager = _RecipeManager
import dev.ultreon.quantum.api.commands.CommandSender as _CommandSender
_CommandSender = _CommandSender
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.server.ServerDisposable as _ServerDisposable
_ServerDisposable = _ServerDisposable
import java.lang.Runnable as Runnable
import dev.ultreon.quantum.gamerule.GameRules as _GameRules
_GameRules = _GameRules
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.resources.ResourceManager as _ResourceManager
_ResourceManager = _ResourceManager
from builtins import object
import dev.ultreon.quantum.server.player.CachedPlayer as _CachedPlayer
_CachedPlayer = _CachedPlayer
try:
    from pyquantum import log
except ImportError:
    log = _import_once("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import java.util.concurrent.ScheduledFuture as _ScheduledFuture
_ScheduledFuture = _ScheduledFuture
import java.lang.Throwable as Throwable
import java.util.stream.Stream as Stream
import dev.ultreon.quantum.server.QuantumServer as _QuantumServer
_QuantumServer = _QuantumServer
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
 
class IntegratedServer():
    """dev.ultreon.quantum.client.IntegratedServer"""
 
    @staticmethod
    def _wrap(java_value: _IntegratedServer) -> 'IntegratedServer':
        return IntegratedServer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntegratedServer):
        """
        Dynamic initializer for IntegratedServer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntegratedServer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntegratedServer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.server.QuantumServer.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @overload
    def savePlayer(self):
        """public void dev.ultreon.quantum.client.IntegratedServer.savePlayer()"""
        super(IntegratedServer, self).savePlayer()

    @overload
    def getCacheablePlayer(self, arg0: 'UUID') -> 'player.CacheablePlayer':
        """public dev.ultreon.quantum.server.player.CacheablePlayer dev.ultreon.quantum.server.QuantumServer.getCacheablePlayer(java.util.UUID)"""
        return 'player.CacheablePlayer'._wrap(super(_server.QuantumServer, self).getCacheablePlayer(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def onDisconnected(self, arg0: 'ServerPlayer', arg1: str):
        """public void dev.ultreon.quantum.server.QuantumServer.onDisconnected(dev.ultreon.quantum.server.player.ServerPlayer,java.lang.String)"""
        super(_server.QuantumServer, self).onDisconnected(arg0, arg1)

    @override
    @overload
    def save(self, arg0: bool):
        """public void dev.ultreon.quantum.client.IntegratedServer.save(boolean) throws java.io.IOException"""
        super(_IntegratedServer, self).save(_boolean.valueOf(arg0))

    @overload
    def disposeOnClose(self, arg0: 'ServerDisposable') -> 'server.ServerDisposable':
        """public <T extends dev.ultreon.quantum.server.ServerDisposable> T dev.ultreon.quantum.server.QuantumServer.disposeOnClose(T)"""
        return 'server.ServerDisposable'._wrap(super(_server.QuantumServer, self).disposeOnClose(arg0))

    @override
    @overload
    def pollAll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.pollAll()"""
        super(util.PollingExecutorService, self).pollAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getGameVersion(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.QuantumServer.getGameVersion()"""
        return str._wrap(super(server.QuantumServer, self).getGameVersion())

    @override
    @overload
    def sendChunk(self, arg0: 'ChunkPos', arg1: 'Chunk'):
        """public void dev.ultreon.quantum.server.QuantumServer.sendChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk) throws java.io.IOException"""
        super(_server.QuantumServer, self).sendChunk(arg0, arg1)

    @override
    @overload
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isRunning()"""
        return bool._wrap(super(server.QuantumServer, self).isRunning())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isDedicated(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isDedicated()"""
        return bool._wrap(super(server.QuantumServer, self).isDedicated())

    @override
    @overload
    def isTerminated(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isTerminated()"""
        return bool._wrap(super(util.PollingExecutorService, self).isTerminated())

    @override
    @overload
    def poll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.poll()"""
        super(util.PollingExecutorService, self).poll()

    @staticmethod
    @overload
    def get() -> 'server.QuantumServer':
        """public static dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.server.QuantumServer.get()"""
        return server.QuantumServer._wrap(_QuantumServer.get())

    @staticmethod
    @overload
    def minutes2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.minutes2ticks(float)"""
        return int._wrap(_QuantumServer.minutes2ticks(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def hours2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.hours2ticks(float)"""
        return int._wrap(_QuantumServer.hours2ticks(_float.valueOf(arg0)))

    @override
    @overload
    def isIntegrated(self) -> bool:
        """public boolean dev.ultreon.quantum.client.IntegratedServer.isIntegrated()"""
        return bool._wrap(super(IntegratedServer, self).isIntegrated())

    @override
    @overload
    def placePlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.client.IntegratedServer.placePlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_IntegratedServer, self).placePlayer(arg0)

    @override
    @overload
    def crash(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.client.IntegratedServer.crash(dev.ultreon.quantum.crash.CrashLog)"""
        super(_IntegratedServer, self).crash(arg0)

    @override
    @overload
    def getConsoleSender(self) -> 'commands.CommandSender':
        """public dev.ultreon.quantum.api.commands.CommandSender dev.ultreon.quantum.server.QuantumServer.getConsoleSender()"""
        return 'commands.CommandSender'._wrap(super(server.QuantumServer, self).getConsoleSender())

    @overload
    def loadPlayer(self, arg0: 'LocalPlayer'):
        """public void dev.ultreon.quantum.client.IntegratedServer.loadPlayer(dev.ultreon.quantum.client.player.LocalPlayer)"""
        super(_IntegratedServer, self).loadPlayer(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def invoke(arg0: 'Runnable') -> 'CompletableFuture':
        """public static java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.server.QuantumServer.invoke(java.lang.Runnable)"""
        return CompletableFuture._wrap(_QuantumServer.invoke(arg0))

    @staticmethod
    @overload
    def invoke(arg0: 'Callable') -> 'CompletableFuture':
        """public static <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.server.QuantumServer.invoke(java.util.concurrent.Callable<T>)"""
        return CompletableFuture._wrap(_QuantumServer.invoke(arg0))

    @overload
    def getWorld(self, arg0: 'Identifier') -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.server.QuantumServer.getWorld(dev.ultreon.quantum.util.Identifier)"""
        return 'world.ServerWorld'._wrap(super(_server.QuantumServer, self).getWorld(arg0))

    @overload
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit') -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_util.PollingExecutorService, self).awaitTermination(_long.valueOf(arg0), arg1))

    @property
    def profiler(self) -> Profiler:
        return Profiler._wrap(super(_PollingExecutorService).profiler())

    @overload
    def getPlayer(self, arg0: 'UUID') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.getPlayer(java.util.UUID)"""
        return 'player.ServerPlayer'._wrap(super(_server.QuantumServer, self).getPlayer(arg0))

    @overload
    def isOpenToLan(self) -> bool:
        """public boolean dev.ultreon.quantum.client.IntegratedServer.isOpenToLan()"""
        return bool._wrap(super(IntegratedServer, self).isOpenToLan())

    @staticmethod
    @overload
    def seconds2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.seconds2ticks(float)"""
        return int._wrap(_QuantumServer.seconds2ticks(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Callable') -> object:
        """public static <T> T dev.ultreon.quantum.server.QuantumServer.invokeAndWait(java.util.concurrent.Callable<T>)"""
        return object._wrap(_QuantumServer.invokeAndWait(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.IntegratedServer.toString()"""
        return str._wrap(super(IntegratedServer, self).toString())

    @override
    @overload
    def getCurrentTps(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getCurrentTps()"""
        return int._wrap(super(server.QuantumServer, self).getCurrentTps())

    @overload
    def invokeAll(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit)"""
        return 'List'._wrap(super(_util.PollingExecutorService, self).invokeAll(arg0, _long.valueOf(arg1), arg2))

    @overload
    def hasPlayedBefore(self, arg0: 'CacheablePlayer') -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.hasPlayedBefore(dev.ultreon.quantum.server.player.CacheablePlayer)"""
        return bool._wrap(super(_server.QuantumServer, self).hasPlayedBefore(arg0))

    @override
    @overload
    def handleChunkLoadFailure(self, arg0: 'ChunkPos', arg1: str):
        """public void dev.ultreon.quantum.client.IntegratedServer.handleChunkLoadFailure(dev.ultreon.quantum.world.ChunkPos,java.lang.String)"""
        super(_IntegratedServer, self).handleChunkLoadFailure(arg0, arg1)

    @overload
    def getCachedPlayer(self, arg0: 'UUID') -> 'player.CachedPlayer':
        """public dev.ultreon.quantum.server.player.CachedPlayer dev.ultreon.quantum.server.QuantumServer.getCachedPlayer(java.util.UUID)"""
        return 'player.CachedPlayer'._wrap(super(_server.QuantumServer, self).getCachedPlayer(arg0))

    @overload
    def getCacheablePlayer(self, arg0: str) -> 'player.CacheablePlayer':
        """public dev.ultreon.quantum.server.player.CacheablePlayer dev.ultreon.quantum.server.QuantumServer.getCacheablePlayer(java.lang.String)"""
        return 'player.CacheablePlayer'._wrap(super(_server.QuantumServer, self).getCacheablePlayer(arg0))

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> dev.ultreon.quantum.util.PollingExecutorService.shutdownNow()"""
        return 'List'._wrap(super(util.PollingExecutorService, self).shutdownNow())

    @overload
    def schedule(self, arg0: 'Runnable', arg1: int, arg2: 'TimeUnit') -> 'ScheduledFuture':
        """public java.util.concurrent.ScheduledFuture<?> dev.ultreon.quantum.server.QuantumServer.schedule(java.lang.Runnable,long,java.util.concurrent.TimeUnit)"""
        return 'ScheduledFuture'._wrap(super(_server.QuantumServer, self).schedule(arg0, _long.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getNetworker(self) -> 'network.Networker':
        """public dev.ultreon.quantum.network.Networker dev.ultreon.quantum.server.QuantumServer.getNetworker()"""
        return 'network.Networker'._wrap(super(server.QuantumServer, self).getNetworker())

    @overload
    def invokeAll(self, arg0: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>)"""
        return 'List'._wrap(super(_util.PollingExecutorService, self).invokeAll(arg0))

    @overload
    def openToLan(self):
        """public void dev.ultreon.quantum.client.IntegratedServer.openToLan()"""
        super(IntegratedServer, self).openToLan()

    @override
    @overload
    def getStorage(self) -> 'world.WorldStorage':
        """public dev.ultreon.quantum.world.WorldStorage dev.ultreon.quantum.server.QuantumServer.getStorage()"""
        return 'world.WorldStorage'._wrap(super(server.QuantumServer, self).getStorage())

    @override
    @overload
    def getPlayerCount(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getPlayerCount()"""
        return int._wrap(super(server.QuantumServer, self).getPlayerCount())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def handleWorldSaveError(self, arg0: 'Exception'):
        """public void dev.ultreon.quantum.client.IntegratedServer.handleWorldSaveError(java.lang.Exception)"""
        super(_IntegratedServer, self).handleWorldSaveError(arg0)

    @override
    @overload
    def start(self):
        """public void dev.ultreon.quantum.client.IntegratedServer.start()"""
        super(IntegratedServer, self).start()

    @override
    @overload
    def getHost(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.IntegratedServer.getHost()"""
        return 'UUID'._wrap(super(IntegratedServer, self).getHost())

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Runnable'):
        """public static void dev.ultreon.quantum.server.QuantumServer.invokeAndWait(java.lang.Runnable)"""
        _QuantumServer.invokeAndWait(arg0)

    @override
    @overload
    def isInitialChunksLoaded(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isInitialChunksLoaded()"""
        return bool._wrap(super(server.QuantumServer, self).isInitialChunksLoaded())

    @override
    @overload
    def getRecipeManager(self) -> 'recipe.RecipeManager':
        """public dev.ultreon.quantum.recipe.RecipeManager dev.ultreon.quantum.server.QuantumServer.getRecipeManager()"""
        return 'recipe.RecipeManager'._wrap(super(server.QuantumServer, self).getRecipeManager())

    @overload
    def getCachedPlayer(self, arg0: str) -> 'player.CachedPlayer':
        """public dev.ultreon.quantum.server.player.CachedPlayer dev.ultreon.quantum.server.QuantumServer.getCachedPlayer(java.lang.String)"""
        return 'player.CachedPlayer'._wrap(super(_server.QuantumServer, self).getCachedPlayer(arg0))

    @override
    @overload
    def getPlayers(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayers()"""
        return 'Collection'._wrap(super(server.QuantumServer, self).getPlayers())

    @overload
    def submit(self, arg0: 'Callable') -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'CompletableFuture'._wrap(super(_util.PollingExecutorService, self).submit(arg0))

    @overload
    def getEntity(self, arg0: int, *arg1: 'entity.Entity') -> 'entity.Entity':
        """public final <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.server.QuantumServer.getEntity(int,T...)"""
        return 'entity.Entity'._wrap(super(_server.QuantumServer, self).getEntity(_int.valueOf(arg0), arg1))

    @override
    @overload
    def getEntityRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getEntityRenderDistance()"""
        return int._wrap(super(server.QuantumServer, self).getEntityRenderDistance())

    @override
    @overload
    def shutdown(self):
        """public void dev.ultreon.quantum.client.IntegratedServer.shutdown()"""
        super(IntegratedServer, self).shutdown()

    @override
    @overload
    def execute(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.util.PollingExecutorService.execute(java.lang.Runnable)"""
        super(_util.PollingExecutorService, self).execute(arg0)

    @overload
    def loadPlayer(self, arg0: str, arg1: 'UUID', arg2: 'IConnection') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.loadPlayer(java.lang.String,java.util.UUID,dev.ultreon.quantum.network.system.IConnection)"""
        return 'player.ServerPlayer'._wrap(super(_server.QuantumServer, self).loadPlayer(arg0, arg1, arg2))

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isShutdown()"""
        return bool._wrap(super(util.PollingExecutorService, self).isShutdown())

    @overload
    def __init__(self, arg0: 'WorldStorage'):
        """public dev.ultreon.quantum.client.IntegratedServer(dev.ultreon.quantum.world.WorldStorage)"""
        val = _IntegratedServer(arg0)
        self.__wrapper = val

    @override
    @overload
    def onInitialChunksLoaded(self):
        """public void dev.ultreon.quantum.client.IntegratedServer.onInitialChunksLoaded()"""
        super(IntegratedServer, self).onInitialChunksLoaded()

    @overload
    def invokeAny(self, arg0: 'Collection') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_util.PollingExecutorService, self).invokeAny(arg0))

    @override
    @overload
    def getGameRules(self) -> 'gamerule.GameRules':
        """public dev.ultreon.quantum.gamerule.GameRules dev.ultreon.quantum.server.QuantumServer.getGameRules()"""
        return 'gamerule.GameRules'._wrap(super(server.QuantumServer, self).getGameRules())

    @overload
    def getPlayer(self, arg0: str) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.getPlayer(java.lang.String)"""
        return 'player.ServerPlayer'._wrap(super(_server.QuantumServer, self).getPlayer(arg0))

    @override
    @overload
    def fatalCrash(self, arg0: 'Throwable'):
        """public void dev.ultreon.quantum.client.IntegratedServer.fatalCrash(java.lang.Throwable)"""
        super(_IntegratedServer, self).fatalCrash(arg0)

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.client.IntegratedServer.close()"""
        super(IntegratedServer, self).close()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getPlayersInChunk(self, arg0: 'ChunkPos') -> 'Stream':
        """public java.util.stream.Stream<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayersInChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Stream'._wrap(super(_server.QuantumServer, self).getPlayersInChunk(arg0))

    @override
    @overload
    def getWorlds(self) -> 'Collection':
        """public java.util.Collection<? extends dev.ultreon.quantum.world.World> dev.ultreon.quantum.server.QuantumServer.getWorlds()"""
        return 'Collection'._wrap(super(server.QuantumServer, self).getWorlds())

    @override
    @overload
    def load(self):
        """public void dev.ultreon.quantum.server.QuantumServer.load() throws java.io.IOException"""
        super(server.QuantumServer, self).load()

    @override
    @overload
    def getPort(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getPort()"""
        return int._wrap(super(server.QuantumServer, self).getPort())

    @override
    @overload
    def crash(self, arg0: 'Throwable'):
        """public void dev.ultreon.quantum.server.QuantumServer.crash(java.lang.Throwable)"""
        super(_server.QuantumServer, self).crash(arg0)

    @override
    @overload
    def getWorld(self) -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.server.QuantumServer.getWorld()"""
        return 'world.ServerWorld'._wrap(super(server.QuantumServer, self).getWorld())

    @staticmethod
    @overload
    def isOnServerThread() -> bool:
        """public static boolean dev.ultreon.quantum.server.QuantumServer.isOnServerThread()"""
        return bool._wrap(_QuantumServer.isOnServerThread())

    @override
    @overload
    def run(self):
        """public void dev.ultreon.quantum.server.QuantumServer.run()"""
        super(server.QuantumServer, self).run()

    @overload
    def submit(self, arg0: 'Runnable', arg1: object) -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable,T)"""
        return 'CompletableFuture'._wrap(super(_util.PollingExecutorService, self).submit(arg0, arg1))

    @override
    @overload
    def addPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.server.QuantumServer.addPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_server.QuantumServer, self).addPlayer(arg0)

    @override
    @overload
    def getCachedPlayers(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.server.player.CachedPlayer> dev.ultreon.quantum.server.QuantumServer.getCachedPlayers()"""
        return 'List'._wrap(super(server.QuantumServer, self).getCachedPlayers())

    @overload
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_util.PollingExecutorService, self).invokeAny(arg0, _long.valueOf(arg1), arg2))

    @override
    @overload
    def getRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.client.IntegratedServer.getRenderDistance()"""
        return int._wrap(super(IntegratedServer, self).getRenderDistance())

    @override
    @overload
    def getDefaultPermissions(self) -> 'player.PermissionMap':
        """public dev.ultreon.quantum.server.player.PermissionMap dev.ultreon.quantum.server.QuantumServer.getDefaultPermissions()"""
        return 'player.PermissionMap'._wrap(super(server.QuantumServer, self).getDefaultPermissions())

    @overload
    def submit(self, arg0: 'Runnable') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable)"""
        return 'CompletableFuture'._wrap(super(_util.PollingExecutorService, self).submit(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getClient(self) -> 'QuantumClient':
        """public dev.ultreon.quantum.client.QuantumClient dev.ultreon.quantum.client.IntegratedServer.getClient()"""
        return 'QuantumClient'._wrap(super(IntegratedServer, self).getClient())

    @override
    @overload
    def getMaxPlayers(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getMaxPlayers()"""
        return int._wrap(super(server.QuantumServer, self).getMaxPlayers())

    @overload
    def getEntity(self, arg0: 'UUID') -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.server.QuantumServer.getEntity(java.util.UUID)"""
        return 'entity.Entity'._wrap(super(_server.QuantumServer, self).getEntity(arg0))

    @override
    @overload
    def getOnlineTicks(self) -> int:
        """public long dev.ultreon.quantum.server.QuantumServer.getOnlineTicks()"""
        return int._wrap(super(server.QuantumServer, self).getOnlineTicks())

    @override
    @overload
    def getResourceManager(self) -> 'resources.ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.server.QuantumServer.getResourceManager()"""
        return 'resources.ResourceManager'._wrap(super(server.QuantumServer, self).getResourceManager())

    @override
    @overload
    def getPlayerManager(self) -> 'server.PlayerManager':
        """public dev.ultreon.quantum.server.PlayerManager dev.ultreon.quantum.server.QuantumServer.getPlayerManager()"""
        return 'server.PlayerManager'._wrap(super(server.QuantumServer, self).getPlayerManager())

    @override
    @overload
    def getPlayersByName(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayersByName()"""
        return 'Map'._wrap(super(server.QuantumServer, self).getPlayersByName()) 
 
 
# CLASS: dev.ultreon.quantum.client.NullClipboard
from builtins import str
import dev.ultreon.quantum.client.NullClipboard as _NullClipboard
_NullClipboard = _NullClipboard
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.IClipboard as _IClipboard
_IClipboard = _IClipboard
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NullClipboard():
    """dev.ultreon.quantum.client.NullClipboard"""
 
    @staticmethod
    def _wrap(java_value: _NullClipboard) -> 'NullClipboard':
        return NullClipboard(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NullClipboard):
        """
        Dynamic initializer for NullClipboard.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NullClipboard__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NullClipboard__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def paste(self) -> str:
        """public default java.lang.String dev.ultreon.quantum.client.IClipboard.paste()"""
        return str._wrap(super(IClipboard, self).paste())

    @override
    @overload
    def copy(self, arg0: 'BufferedImage'):
        """public void dev.ultreon.quantum.client.NullClipboard.copy(java.awt.image.BufferedImage)"""
        super(_NullClipboard, self).copy(arg0)

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.NullClipboard()"""
        val = _NullClipboard()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.NullClipboard()"""
        val = _NullClipboard()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def copy(self, arg0: str):
        """public void dev.ultreon.quantum.client.NullClipboard.copy(java.lang.String)"""
        super(_NullClipboard, self).copy(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.RhinoExceptionScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.UIContainer as _UIContainer
_UIContainer = _UIContainer
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import dev.ultreon.quantum.client.RhinoExceptionScreen as _RhinoExceptionScreen
_RhinoExceptionScreen = _RhinoExceptionScreen
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.gui.widget.layout.Layout as _Layout
_Layout = _Layout
import dev.ultreon.quantum.client.gui.Screen as _Screen
_Screen = _Screen
try:
    from pyquantum import component
except ImportError:
    component = _import_once("pyquantum.component")

import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = _import_once("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.client.gui.Dialog as _Dialog
_Dialog = _Dialog
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.widget.Widget as _Widget
_Widget = _Widget
import dev.ultreon.quantum.client.gui.Position as _Position
_Position = _Position
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RhinoExceptionScreen():
    """dev.ultreon.quantum.client.RhinoExceptionScreen"""
 
    @staticmethod
    def _wrap(java_value: _RhinoExceptionScreen) -> 'RhinoExceptionScreen':
        return RhinoExceptionScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RhinoExceptionScreen):
        """
        Dynamic initializer for RhinoExceptionScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RhinoExceptionScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RhinoExceptionScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(_gui.Screen, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'._wrap(super(gui.Screen, self).getTitle())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_widget.Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_widget.Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_widget.Widget, self).setPos(arg0)

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'._wrap(super(_widget.UIContainer, self).getWidgetsAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(widget.Widget, self).getX())

    @overload
    def title(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).title(arg0))

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_widget.Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(widget.Widget, self).isFocused())

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_widget.Widget, self).onRevalidate(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(widget.Widget, self).isEnabled())

    @override
    @overload
    def getDialog(self) -> 'gui.Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'gui.Dialog'._wrap(super(gui.Screen, self).getDialog())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_widget.Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(_gui.Screen, self).closeDialog(arg0)

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.client.RhinoExceptionScreen(java.util.List<org.mozilla.javascript.RhinoException>)"""
        val = _RhinoExceptionScreen(arg0)
        self.__wrapper = val

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'._wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str._wrap(super(gui.Screen, self).getRawTitle())

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool._wrap(super(_gui.Screen, self).onClose(arg0))

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_widget.UIContainer, self).renderChild(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_widget.Widget, self).setSize(arg0)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'._wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str._wrap(super(gui.Screen, self).getName())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool._wrap(_Widget.isPosWithin(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_widget.Widget, self).height(_int.valueOf(arg0))

    @override
    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool._wrap(super(gui.Screen, self).back())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_widget.Widget, self).setEnabled(_boolean.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(widget.Widget, self).isClickable())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(widget.Widget, self).getWidth())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_widget.Widget, self).setBounds(arg0)

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_widget.Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canCloseWithEsc()"""
        return bool._wrap(super(gui.Screen, self).canCloseWithEsc())

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(widget.Widget, self).isHovered())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(_Screen).parentScreen(value)

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'._wrap(super(gui.Screen, self).path())

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.RhinoExceptionScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_RhinoExceptionScreen, self).build(arg0)

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_widget.Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_widget.Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(_widget.UIContainer, self).setLayout(arg0)

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(_Screen).directHovered(value)

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(widget.Widget, self).getPreferredHeight())

    @override
    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(_gui.Screen, self).init(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_widget.Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(_gui.Screen, self).showDialog(arg0)

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'._wrap(super(_widget.UIContainer, self).getWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @property
    def focused(self, value: 'widget.Widget'):
        super(_Screen).focused(value)

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool._wrap(super(gui.Screen, self).isHoveringClickable())

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'._wrap(super(_widget.UIContainer, self).position(arg0))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_widget.Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_widget.Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'._wrap(super(widget.UIContainer, self).getLayout())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'._wrap(super(_widget.UIContainer, self).bounds(arg0))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_widget.Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).title(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool._wrap(super(_gui.Screen, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_widget.UIContainer, self).remove(arg0)

    @property
    def focused(self) -> Widget:
        return Widget._wrap(super(_Screen).focused())

    @property
    def directHovered(self) -> Widget:
        return Widget._wrap(super(_Screen).directHovered())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_widget.Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(widget.Widget, self).componentRegistry())

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'._wrap(super(_gui.Screen, self).add(arg0))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_widget.Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool._wrap(super(_gui.Screen, self).filesDropped(arg0))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool._wrap(super(_gui.Screen, self).charType(_char.valueOf(arg0)))

    @property
    def parentScreen(self) -> Screen:
        return Screen._wrap(super(_Screen).parentScreen())

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'._wrap(super(_widget.UIContainer, self).getExactWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_widget.Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(widget.Widget, self).getPreferredSize())

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canClose()"""
        return bool._wrap(super(gui.Screen, self).canClose())

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.GameEnvironment
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import dev.ultreon.quantum.client.GameEnvironment as _GameEnvironment
_GameEnvironment = _GameEnvironment
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GameEnvironment():
    """dev.ultreon.quantum.client.GameEnvironment"""
 
    @staticmethod
    def _wrap(java_value: _GameEnvironment) -> 'GameEnvironment':
        return GameEnvironment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GameEnvironment):
        """
        Dynamic initializer for GameEnvironment.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GameEnvironment__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GameEnvironment__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'GameEnvironment':
        """public static dev.ultreon.quantum.client.GameEnvironment dev.ultreon.quantum.client.GameEnvironment.valueOf(java.lang.String)"""
        return GameEnvironment._wrap(_GameEnvironment.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def values() -> List['GameEnvironment']:
        """public static dev.ultreon.quantum.client.GameEnvironment[] dev.ultreon.quantum.client.GameEnvironment.values()"""
        return List[GameEnvironment]._wrap(_GameEnvironment.values())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


GameEnvironment.DEVELOPMENT = GameEnvironment._wrap(_DEVELOPMENT.DEVELOPMENT)

GameEnvironment.NORMAL = GameEnvironment._wrap(_NORMAL.NORMAL)

GameEnvironment.PACKAGED = GameEnvironment._wrap(_PACKAGED.PACKAGED)

GameEnvironment.UNKNOWN = GameEnvironment._wrap(_UNKNOWN.UNKNOWN) 
 
 
# CLASS: dev.ultreon.quantum.client.FontManager
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.FontManager as _FontManager
_FontManager = _FontManager
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import dev.ultreon.quantum.client.font.Font as _Font
_Font = _Font
try:
    from pyquantum.client import font
except ImportError:
    font = _import_once("pyquantum.client.font")

try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FontManager():
    """dev.ultreon.quantum.client.FontManager"""
 
    @staticmethod
    def _wrap(java_value: _FontManager) -> 'FontManager':
        return FontManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FontManager):
        """
        Dynamic initializer for FontManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FontManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FontManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def registerFonts(self, arg0: 'ResourceManager'):
        """public void dev.ultreon.quantum.client.FontManager.registerFonts(dev.ultreon.quantum.resources.ResourceManager)"""
        super(_FontManager, self).registerFonts(arg0)

    @overload
    def getFont(self, arg0: 'Identifier') -> 'font.Font':
        """public dev.ultreon.quantum.client.font.Font dev.ultreon.quantum.client.FontManager.getFont(dev.ultreon.quantum.util.Identifier)"""
        return 'font.Font'._wrap(super(_FontManager, self).getFont(arg0))

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
    def registerFont(self, arg0: 'Identifier', arg1: 'Font') -> 'font.Font':
        """public dev.ultreon.quantum.client.font.Font dev.ultreon.quantum.client.FontManager.registerFont(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.font.Font)"""
        return 'font.Font'._wrap(super(_FontManager, self).registerFont(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def get() -> 'FontManager':
        """public static dev.ultreon.quantum.client.FontManager dev.ultreon.quantum.client.FontManager.get()"""
        return FontManager._wrap(_FontManager.get())

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

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.FontManager.dispose()"""
        super(FontManager, self).dispose()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.Metadata
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.Metadata as _Metadata
_Metadata = _Metadata
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Metadata():
    """dev.ultreon.quantum.client.Metadata"""
 
    @staticmethod
    def _wrap(java_value: _Metadata) -> 'Metadata':
        return Metadata(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Metadata):
        """
        Dynamic initializer for Metadata.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Metadata__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Metadata__wrapper":
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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.Metadata()"""
        val = _Metadata()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.Metadata()"""
        val = _Metadata()
        self.__wrapper = val

    @staticmethod
    @overload
    def get() -> 'Metadata':
        """public static dev.ultreon.quantum.client.Metadata dev.ultreon.quantum.client.Metadata.get()"""
        return Metadata._wrap(_Metadata.get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.ClientModInit
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.ClientModInit as _ClientModInit
_ClientModInit = _ClientModInit
 
class ClientModInit():
    """dev.ultreon.quantum.client.ClientModInit"""
 
    @staticmethod
    def _wrap(java_value: _ClientModInit) -> 'ClientModInit':
        return ClientModInit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientModInit):
        """
        Dynamic initializer for ClientModInit.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientModInit__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientModInit__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onInitializeClient(self, ):
        """public abstract void dev.ultreon.quantum.client.ClientModInit.onInitializeClient()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.CrashScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.UIContainer as _UIContainer
_UIContainer = _UIContainer
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.gui.widget.layout.Layout as _Layout
_Layout = _Layout
import dev.ultreon.quantum.client.CrashScreen as _CrashScreen
_CrashScreen = _CrashScreen
import dev.ultreon.quantum.client.gui.Screen as _Screen
_Screen = _Screen
try:
    from pyquantum import component
except ImportError:
    component = _import_once("pyquantum.component")

import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = _import_once("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.client.gui.Dialog as _Dialog
_Dialog = _Dialog
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.widget.Widget as _Widget
_Widget = _Widget
import dev.ultreon.quantum.client.gui.Position as _Position
_Position = _Position
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CrashScreen():
    """dev.ultreon.quantum.client.CrashScreen"""
 
    @staticmethod
    def _wrap(java_value: _CrashScreen) -> 'CrashScreen':
        return CrashScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CrashScreen):
        """
        Dynamic initializer for CrashScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CrashScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CrashScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(_gui.Screen, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'._wrap(super(gui.Screen, self).getTitle())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_widget.Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_widget.Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_widget.Widget, self).setPos(arg0)

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'._wrap(super(_widget.UIContainer, self).getWidgetsAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(widget.Widget, self).getX())

    @overload
    def title(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).title(arg0))

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_widget.Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(widget.Widget, self).isFocused())

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_widget.Widget, self).onRevalidate(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(widget.Widget, self).isEnabled())

    @override
    @overload
    def getDialog(self) -> 'gui.Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'gui.Dialog'._wrap(super(gui.Screen, self).getDialog())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_widget.Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(_gui.Screen, self).closeDialog(arg0)

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.client.CrashScreen(java.util.List<dev.ultreon.quantum.crash.CrashLog>)"""
        val = _CrashScreen(arg0)
        self.__wrapper = val

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'._wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str._wrap(super(gui.Screen, self).getRawTitle())

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool._wrap(super(_gui.Screen, self).onClose(arg0))

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_widget.UIContainer, self).renderChild(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_widget.Widget, self).setSize(arg0)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'._wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str._wrap(super(gui.Screen, self).getName())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool._wrap(_Widget.isPosWithin(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_widget.Widget, self).height(_int.valueOf(arg0))

    @override
    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool._wrap(super(gui.Screen, self).back())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_widget.Widget, self).setEnabled(_boolean.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(widget.Widget, self).isClickable())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(widget.Widget, self).getWidth())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_widget.Widget, self).setBounds(arg0)

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.CrashScreen.canCloseWithEsc()"""
        return bool._wrap(super(CrashScreen, self).canCloseWithEsc())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_widget.Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(widget.Widget, self).isHovered())

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(_Screen).parentScreen(value)

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'._wrap(super(gui.Screen, self).path())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_widget.Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_widget.Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(_widget.UIContainer, self).setLayout(arg0)

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(_Screen).directHovered(value)

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(widget.Widget, self).getPreferredHeight())

    @override
    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(_gui.Screen, self).init(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_widget.Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(_gui.Screen, self).showDialog(arg0)

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.CrashScreen.canClose()"""
        return bool._wrap(super(CrashScreen, self).canClose())

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'._wrap(super(_widget.UIContainer, self).getWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @property
    def focused(self, value: 'widget.Widget'):
        super(_Screen).focused(value)

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool._wrap(super(gui.Screen, self).isHoveringClickable())

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'._wrap(super(_widget.UIContainer, self).position(arg0))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_widget.Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_widget.Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'._wrap(super(widget.UIContainer, self).getLayout())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'._wrap(super(_widget.UIContainer, self).bounds(arg0))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_widget.Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).title(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool._wrap(super(_gui.Screen, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_widget.UIContainer, self).remove(arg0)

    @property
    def focused(self) -> Widget:
        return Widget._wrap(super(_Screen).focused())

    @property
    def directHovered(self) -> Widget:
        return Widget._wrap(super(_Screen).directHovered())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_widget.Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(widget.Widget, self).componentRegistry())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.CrashScreen.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_CrashScreen, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'._wrap(super(_gui.Screen, self).add(arg0))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_widget.Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool._wrap(super(_gui.Screen, self).filesDropped(arg0))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool._wrap(super(_gui.Screen, self).charType(_char.valueOf(arg0)))

    @property
    def parentScreen(self) -> Screen:
        return Screen._wrap(super(_Screen).parentScreen())

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'._wrap(super(_widget.UIContainer, self).getExactWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_widget.Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.CrashScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_CrashScreen, self).build(arg0)

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(widget.Widget, self).getPreferredSize())

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.IClipboard
from builtins import str
import dev.ultreon.quantum.client.IClipboard as _IClipboard
_IClipboard = _IClipboard
import java.awt.image.BufferedImage as BufferedImage
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
 
class IClipboard():
    """dev.ultreon.quantum.client.IClipboard"""
 
    @staticmethod
    def _wrap(java_value: _IClipboard) -> 'IClipboard':
        return IClipboard(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IClipboard):
        """
        Dynamic initializer for IClipboard.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IClipboard__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IClipboard__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def paste(self) -> str:
        """public default java.lang.String dev.ultreon.quantum.client.IClipboard.paste()"""
        return str._wrap(super(IClipboard, self).paste())

    @abstractmethod
    def copy(self, arg0: str):
        """public abstract void dev.ultreon.quantum.client.IClipboard.copy(java.lang.String)"""
        pass

    @abstractmethod
    def copy(self, arg0: 'BufferedImage'):
        """public abstract void dev.ultreon.quantum.client.IClipboard.copy(java.awt.image.BufferedImage)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.DisposableContainer
from pyquantum_helper import import_once as _import_once
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import dev.ultreon.quantum.client.DisposableContainer as _DisposableContainer
_DisposableContainer = _DisposableContainer
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Disposable as _Disposable
_Disposable = _Disposable
 
class DisposableContainer():
    """dev.ultreon.quantum.client.DisposableContainer"""
 
    @staticmethod
    def _wrap(java_value: _DisposableContainer) -> 'DisposableContainer':
        return DisposableContainer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DisposableContainer):
        """
        Dynamic initializer for DisposableContainer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DisposableContainer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DisposableContainer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.User as _User
_User = _User
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class User():
    """dev.ultreon.quantum.client.User"""
 
    @staticmethod
    def _wrap(java_value: _User) -> 'User':
        return User(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _User):
        """
        Dynamic initializer for User.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_User__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_User__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.User.toString()"""
        return str._wrap(super(User, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.User.hashCode()"""
        return int._wrap(super(User, self).hashCode())

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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.User.name()"""
        return str._wrap(super(User, self).name())

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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.User(java.lang.String)"""
        val = _User(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.User.equals(java.lang.Object)"""
        return bool._wrap(super(_User, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.InternalApi
import dev.ultreon.quantum.client.InternalApi as _InternalApi
_InternalApi = _InternalApi
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class InternalApi():
    """dev.ultreon.quantum.client.InternalApi"""
 
    @staticmethod
    def _wrap(java_value: _InternalApi) -> 'InternalApi':
        return InternalApi(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InternalApi):
        """
        Dynamic initializer for InternalApi.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InternalApi__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InternalApi__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.String as _String
_String = _String
try:
    from pyquantum.client.render import pipeline
except ImportError:
    pipeline = _import_once("pyquantum.client.render.pipeline")

import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.RenderContext as _RenderContext
_RenderContext = _RenderContext
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

import dev.ultreon.quantum.client.GameRenderer as _GameRenderer
_GameRenderer = _GameRenderer
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GameRenderer():
    """dev.ultreon.quantum.client.GameRenderer"""
 
    @staticmethod
    def _wrap(java_value: _GameRenderer) -> 'GameRenderer':
        return GameRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GameRenderer):
        """
        Dynamic initializer for GameRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GameRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GameRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def render(self, arg0: 'Renderer', arg1: float):
        """public void dev.ultreon.quantum.client.GameRenderer.render(dev.ultreon.quantum.client.gui.Renderer,float)"""
        super(_GameRenderer, self).render(arg0, _float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'QuantumClient', arg1: 'ModelBatch', arg2: 'RenderPipeline'):
        """public dev.ultreon.quantum.client.GameRenderer(dev.ultreon.quantum.client.QuantumClient,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.render.pipeline.RenderPipeline)"""
        val = _GameRenderer(arg0, arg1, arg2)
        self.__wrapper = val

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
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.GameRenderer.resize(int,int)"""
        super(_GameRenderer, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getContext(self) -> 'utils.RenderContext':
        """public com.badlogic.gdx.graphics.g3d.utils.RenderContext dev.ultreon.quantum.client.GameRenderer.getContext()"""
        return 'utils.RenderContext'._wrap(super(GameRenderer, self).getContext())

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
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.OutOfMemoryScreen
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.component.GameComponentHolder as _GameComponentHolder
_GameComponentHolder = _GameComponentHolder
import dev.ultreon.quantum.client.gui.widget.UIContainer as _UIContainer
_UIContainer = _UIContainer
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.util.function.Consumer as Consumer
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.client.gui.widget.layout.Layout as _Layout
_Layout = _Layout
import dev.ultreon.quantum.client.OutOfMemoryScreen as _OutOfMemoryScreen
_OutOfMemoryScreen = _OutOfMemoryScreen
import dev.ultreon.quantum.client.gui.Screen as _Screen
_Screen = _Screen
try:
    from pyquantum import component
except ImportError:
    component = _import_once("pyquantum.component")

import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = _import_once("pyquantum.client.gui.widget.layout")

import java.nio.file.Path as Path
import dev.ultreon.quantum.client.gui.Dialog as _Dialog
_Dialog = _Dialog
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.client.gui.widget.Widget as _Widget
_Widget = _Widget
import dev.ultreon.quantum.client.gui.Position as _Position
_Position = _Position
import dev.ultreon.quantum.client.gui.Size as _Size
_Size = _Size
import dev.ultreon.quantum.client.gui.Bounds as _Bounds
_Bounds = _Bounds
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OutOfMemoryScreen():
    """dev.ultreon.quantum.client.OutOfMemoryScreen"""
 
    @staticmethod
    def _wrap(java_value: _OutOfMemoryScreen) -> 'OutOfMemoryScreen':
        return OutOfMemoryScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OutOfMemoryScreen):
        """
        Dynamic initializer for OutOfMemoryScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OutOfMemoryScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OutOfMemoryScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(_gui.Screen, self).mouseMove(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(_gui.Screen, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'._wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseDrag(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool._wrap(super(_gui.Screen, self).keyRelease(_int.valueOf(arg0)))

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.Screen.onClosed()"""
        super(gui.Screen, self).onClosed()

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mousePress(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'._wrap(super(gui.Screen, self).getTitle())

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(_widget.Widget, self).setPreferredSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(_widget.Widget, self).setPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(_widget.Widget, self).setPos(arg0)

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'._wrap(super(_widget.UIContainer, self).getWidgetsAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int._wrap(super(widget.Widget, self).getX())

    @overload
    def title(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).title(arg0))

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(_widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(_widget.Widget, self).width(_int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool._wrap(super(widget.Widget, self).isFocused())

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(_widget.Widget, self).onRevalidate(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool._wrap(super(widget.Widget, self).isEnabled())

    @override
    @overload
    def getDialog(self) -> 'gui.Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'gui.Dialog'._wrap(super(gui.Screen, self).getDialog())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int._wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(_widget.Widget, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(_gui.Screen, self).closeDialog(arg0)

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseRelease(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool._wrap(super(_gui.Screen, self).mouseWheel(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).renderChildren(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'._wrap(super(widget.UIContainer, self).getWidgets())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int._wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'._wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(_widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str._wrap(super(gui.Screen, self).getRawTitle())

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool._wrap(super(_gui.Screen, self).onClose(arg0))

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_widget.UIContainer, self).renderChild(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(_widget.Widget, self).setSize(arg0)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool._wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_gui.Screen, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'._wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str._wrap(super(gui.Screen, self).getName())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool._wrap(_Widget.isPosWithin(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(_widget.Widget, self).height(_int.valueOf(arg0))

    @override
    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool._wrap(super(gui.Screen, self).back())

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(_widget.Widget, self).setEnabled(_boolean.valueOf(arg0))

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool._wrap(super(widget.Widget, self).isClickable())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int._wrap(super(widget.Widget, self).getWidth())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(_widget.Widget, self).setBounds(arg0)

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int._wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(_widget.Widget, self).setPreferredWidth(_int.valueOf(arg0))

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canCloseWithEsc()"""
        return bool._wrap(super(gui.Screen, self).canCloseWithEsc())

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool._wrap(super(widget.Widget, self).isHovered())

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_widget.UIContainer, self).renderWidget(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(_Screen).parentScreen(value)

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'._wrap(super(gui.Screen, self).path())

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool._wrap(super(_widget.Widget, self).isWithinBounds(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(_widget.Widget, self).x(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(_widget.UIContainer, self).setLayout(arg0)

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(_Screen).directHovered(value)

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int._wrap(super(widget.Widget, self).getPreferredHeight())

    @override
    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(_gui.Screen, self).init(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(_widget.Widget, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(_gui.Screen, self).showDialog(arg0)

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'._wrap(super(_widget.UIContainer, self).getWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @property
    def focused(self, value: 'widget.Widget'):
        super(_Screen).focused(value)

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool._wrap(super(gui.Screen, self).isHoveringClickable())

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'._wrap(super(_widget.UIContainer, self).position(arg0))

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'._wrap(super(_widget.Widget, self).getComponent(arg0, arg1))

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int._wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(_widget.Widget, self).setPreferredHeight(_int.valueOf(arg0))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'._wrap(super(widget.UIContainer, self).getLayout())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'._wrap(super(_widget.UIContainer, self).bounds(arg0))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(_widget.Widget, self).setPreferredX(_int.valueOf(arg0))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).title(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool._wrap(super(_gui.Screen, self).keyPress(_int.valueOf(arg0)))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_widget.UIContainer, self).remove(arg0)

    @property
    def focused(self) -> Widget:
        return Widget._wrap(super(_Screen).focused())

    @property
    def directHovered(self) -> Widget:
        return Widget._wrap(super(_Screen).directHovered())

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseClick(int,int,int,int)"""
        return bool._wrap(super(_gui.Screen, self).mouseClick(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(_widget.Widget, self).y(_int.valueOf(arg0))

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'._wrap(super(widget.Widget, self).componentRegistry())

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public void dev.ultreon.quantum.client.OutOfMemoryScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(_OutOfMemoryScreen, self).build(arg0)

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'._wrap(super(_gui.Screen, self).add(arg0))

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(_widget.Widget, self).setPreferredPos(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool._wrap(super(_gui.Screen, self).filesDropped(arg0))

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool._wrap(super(_gui.Screen, self).charType(_char.valueOf(arg0)))

    @property
    def parentScreen(self) -> Screen:
        return Screen._wrap(super(_Screen).parentScreen())

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'._wrap(super(_widget.UIContainer, self).getExactWidgetAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int._wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'._wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(_widget.Widget, self).setPreferredY(_int.valueOf(arg0))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'._wrap(super(widget.Widget, self).getPreferredSize())

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canClose()"""
        return bool._wrap(super(gui.Screen, self).canClose())

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'._wrap(super(_gui.Screen, self).titleTranslation(arg0))


widget.UIContainer.ROOT = widget.UIContainer._wrap(_ROOT.ROOT) 
 
 
# CLASS: dev.ultreon.quantum.client.Screenshot
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

import com.badlogic.gdx.graphics.Pixmap as _Pixmap
_Pixmap = _Pixmap
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import dev.ultreon.quantum.client.Screenshot as _Screenshot
_Screenshot = _Screenshot
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Screenshot():
    """dev.ultreon.quantum.client.Screenshot"""
 
    @staticmethod
    def _wrap(java_value: _Screenshot) -> 'Screenshot':
        return Screenshot(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Screenshot):
        """
        Dynamic initializer for Screenshot.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Screenshot__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Screenshot__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.Screenshot.dispose()"""
        super(Screenshot, self).dispose()

    @overload
    def save(self, arg0: 'Path'):
        """public void dev.ultreon.quantum.client.Screenshot.save(java.nio.file.Path)"""
        super(_Screenshot, self).save(arg0)

    @overload
    def getPixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap dev.ultreon.quantum.client.Screenshot.getPixmap()"""
        return 'graphics.Pixmap'._wrap(super(Screenshot, self).getPixmap())

    @overload
    def saveAndDispose(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.Screenshot.saveAndDispose(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_Screenshot, self).saveAndDispose(arg0))

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
    def isDisposed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.Screenshot.isDisposed()"""
        return bool._wrap(super(Screenshot, self).isDisposed())

    @staticmethod
    @overload
    def grab(arg0: int, arg1: int) -> 'Screenshot':
        """public static dev.ultreon.quantum.client.Screenshot dev.ultreon.quantum.client.Screenshot.grab(int,int)"""
        return Screenshot._wrap(_Screenshot.grab(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def save(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.Screenshot.save(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_Screenshot, self).save(arg0))

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
    def __init__(self, arg0: 'Pixmap'):
        """public dev.ultreon.quantum.client.Screenshot(com.badlogic.gdx.graphics.Pixmap)"""
        val = _Screenshot(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.client.HardwareMonitor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.HardwareMonitor as _HardwareMonitor
_HardwareMonitor = _HardwareMonitor
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HardwareMonitor():
    """dev.ultreon.quantum.client.HardwareMonitor"""
 
    @staticmethod
    def _wrap(java_value: _HardwareMonitor) -> 'HardwareMonitor':
        return HardwareMonitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HardwareMonitor):
        """
        Dynamic initializer for HardwareMonitor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HardwareMonitor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HardwareMonitor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.HardwareMonitor()"""
        val = _HardwareMonitor()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.HardwareMonitor()"""
        val = _HardwareMonitor()
        self.__wrapper = val

        @staticmethod
        @overload
        def start():
            """public static synchronized void dev.ultreon.quantum.client.HardwareMonitor.start()"""
            _HardwareMonitor.start()

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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
 
 
# CLASS: dev.ultreon.quantum.client.QuantumClient
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.texture.TextureManager as _TextureManager
_TextureManager = _TextureManager
import dev.ultreon.quantum.client.gui.Renderer as _Renderer
_Renderer = _Renderer
try:
    from pyquantum.client import player
except ImportError:
    player = _import_once("pyquantum.client.player")

try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import dev.ultreon.quantum.client.management.ShaderProviderManager as _ShaderProviderManager
_ShaderProviderManager = _ShaderProviderManager
try:
    from pyquantum import crash
except ImportError:
    crash = _import_once("pyquantum.crash")

import dev.ultreon.quantum.client.User as _User
_User = _User
import dev.ultreon.quantum.client.gui.Hud as _Hud
_Hud = _Hud
import dev.ultreon.quantum.GameWindow as _GameWindow
_GameWindow = _GameWindow
import dev.ultreon.quantum.client.player.SkinManager as _SkinManager
_SkinManager = _SkinManager
import dev.ultreon.libs.datetime.v0.Duration as _Duration
_Duration = _Duration
import dev.ultreon.quantum.world.WorldStorage as _WorldStorage
_WorldStorage = _WorldStorage
import java.util.concurrent.Callable as Callable
import dev.ultreon.quantum.client.model.block.BlockModel as _BlockModel
_BlockModel = _BlockModel
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.client.config.GameSettings as _GameSettings
_GameSettings = _GameSettings
import com.badlogic.gdx.math.GridPoint2 as _GridPoint2
_GridPoint2 = _GridPoint2
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
try:
    from pyquantum.client import multiplayer
except ImportError:
    multiplayer = _import_once("pyquantum.client.multiplayer")

from builtins import float
try:
    from pyquantum.client.render import pipeline
except ImportError:
    pipeline = _import_once("pyquantum.client.render.pipeline")

try:
    from pyquantum.client import registry
except ImportError:
    registry = _import_once("pyquantum.client.registry")

from typing import List
try:
    from pyquantum.client import sound
except ImportError:
    sound = _import_once("pyquantum.client.sound")

import java.util.concurrent.TimeUnit as TimeUnit
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

try:
    from pyquantum.client import font
except ImportError:
    font = _import_once("pyquantum.client.font")

import dev.ultreon.quantum.client.multiplayer.MultiplayerData as _MultiplayerData
_MultiplayerData = _MultiplayerData
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

import java.util.concurrent.CompletableFuture as CompletableFuture
from builtins import int
import dev.ultreon.quantum.network.system.IConnection as _IConnection
_IConnection = _IConnection
import dev.ultreon.quantum.client.world.ClientWorld as _ClientWorld
_ClientWorld = _ClientWorld
from builtins import type
try:
    from pyquantum.client import atlas
except ImportError:
    atlas = _import_once("pyquantum.client.atlas")

import java.lang.AutoCloseable as _AutoCloseable
_AutoCloseable = _AutoCloseable
import dev.ultreon.quantum.client.Metadata as _Metadata
_Metadata = _Metadata
import dev.ultreon.quantum.util.HitResult as _HitResult
_HitResult = _HitResult
import java.lang.String as _string
import dev.ultreon.quantum.client.input.GameInput as _GameInput
_GameInput = _GameInput
import dev.ultreon.quantum.client.gui.Screen as _Screen
_Screen = _Screen
try:
    from pyquantum.client import management
except ImportError:
    management = _import_once("pyquantum.client.management")

import dev.ultreon.quantum.client.font.Font as _Font
_Font = _Font
import java.util.concurrent.ScheduledFuture as ScheduledFuture
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import dev.ultreon.quantum.debug.profiler.Profiler as _Profiler
_Profiler = _Profiler
import dev.ultreon.quantum.client.input.PlayerInput as _PlayerInput
_PlayerInput = _PlayerInput
import com.badlogic.gdx.assets.AssetManager as _AssetManager
_AssetManager = _AssetManager
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as _RenderPipeline
_RenderPipeline = _RenderPipeline
import dev.ultreon.quantum.client.registry.EntityModelRegistry as _EntityModelRegistry
_EntityModelRegistry = _EntityModelRegistry
import java.lang.Runnable as Runnable
try:
    from pyquantum.client.gui import debug
except ImportError:
    debug = _import_once("pyquantum.client.gui.debug")

import dev.ultreon.quantum.resources.ResourceManager as _ResourceManager
_ResourceManager = _ResourceManager
import java.lang.AutoCloseable as AutoCloseable
from builtins import object
try:
    from pyquantum import log
except ImportError:
    log = _import_once("pyquantum.log")

import dev.ultreon.quantum.client.atlas.TextureAtlas as _TextureAtlas
_TextureAtlas = _TextureAtlas
import dev.ultreon.quantum.client.gui.NotifyManager as _NotifyManager
_NotifyManager = _NotifyManager
import java.util.concurrent.ExecutorService as _ExecutorService
_ExecutorService = _ExecutorService
try:
    from pyquantum.client import item
except ImportError:
    item = _import_once("pyquantum.client.item")

import java.util.concurrent.ScheduledFuture as _ScheduledFuture
_ScheduledFuture = _ScheduledFuture
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

try:
    from pyquantum.client import util
except ImportError:
    util = _import_once("pyquantum.client.util")

import java.lang.Long as _long
import com.badlogic.gdx.utils.Disposable as _Disposable
_Disposable = _Disposable
import java.util.List as List
import dev.ultreon.quantum.client.IntegratedServer as _IntegratedServer
_IntegratedServer = _IntegratedServer
import dev.ultreon.quantum.client.world.WorldRenderer as _WorldRenderer
_WorldRenderer = _WorldRenderer
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.util.Collection as Collection
try:
    from pyquantum.client.model import block
except ImportError:
    block = _import_once("pyquantum.client.model.block")

import dev.ultreon.quantum.client.util.PlayerView as _PlayerView
_PlayerView = _PlayerView
import java.nio.file.Path as _Path
_Path = _Path
try:
    from pyquantum.client import audio
except ImportError:
    audio = _import_once("pyquantum.client.audio")

import dev.ultreon.quantum.client.management.ShaderProgramManager as _ShaderProgramManager
_ShaderProgramManager = _ShaderProgramManager
import java.lang.Boolean as _boolean
try:
    from pyquantum.debug import profiler
except ImportError:
    profiler = _import_once("pyquantum.debug.profiler")

import dev.ultreon.quantum.client.input.GameCamera as _GameCamera
_GameCamera = _GameCamera
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

import dev.ultreon.quantum.client.util.GG as _GG
_GG = _GG
import dev.ultreon.quantum.util.BlockHitResult as _BlockHitResult
_BlockHitResult = _BlockHitResult
from builtins import bool
import dev.ultreon.quantum.client.input.TouchPoint as _TouchPoint
_TouchPoint = _TouchPoint
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

try:
    from pyquantum.client import texture
except ImportError:
    texture = _import_once("pyquantum.client.texture")

import dev.ultreon.quantum.client.IClipboard as _IClipboard
_IClipboard = _IClipboard
import dev.ultreon.quantum.client.gui.debug.DebugOverlay as _DebugOverlay
_DebugOverlay = _DebugOverlay
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

try:
    from pyquantum.client import config
except ImportError:
    config = _import_once("pyquantum.client.config")

import dev.ultreon.quantum.client.sound.ClientSoundRegistry as _ClientSoundRegistry
_ClientSoundRegistry = _ClientSoundRegistry
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.client.player.LocalPlayer as _LocalPlayer
_LocalPlayer = _LocalPlayer
import java.lang.Float as _float
import dev.ultreon.quantum.util.Shutdownable as _Shutdownable
_Shutdownable = _Shutdownable
import java.util.concurrent.CompletableFuture as _CompletableFuture
_CompletableFuture = _CompletableFuture
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.client.QuantumClient as _QuantumClient
_QuantumClient = _QuantumClient
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

import dev.ultreon.quantum.util.PollingExecutorService as _PollingExecutorService
_PollingExecutorService = _PollingExecutorService
import java.lang.Class as _Class
_Class = _Class
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.config.ClientConfig as _ClientConfig
_ClientConfig = _ClientConfig
import dev.ultreon.quantum.client.management.MaterialManager as _MaterialManager
_MaterialManager = _MaterialManager
import dev.ultreon.quantum.client.GameEnvironment as _GameEnvironment
_GameEnvironment = _GameEnvironment
try:
    from pycorelibs.datetime import v0
except ImportError:
    v0 = _import_once("pycorelibs.datetime.v0")

import dev.ultreon.quantum.client.item.ItemRenderer as _ItemRenderer
_ItemRenderer = _ItemRenderer
import dev.ultreon.quantum.client.config.ConfigScreenFactory as _ConfigScreenFactory
_ConfigScreenFactory = _ConfigScreenFactory
from builtins import str
try:
    from pyquantum.debug import inspect
except ImportError:
    inspect = _import_once("pyquantum.debug.inspect")

from pyquantum_helper import override
import dev.ultreon.quantum.client.registry.EntityRendererRegistry as _EntityRendererRegistry
_EntityRendererRegistry = _EntityRendererRegistry
import java.nio.file.Path as Path
import com.badlogic.gdx.graphics.g3d.Environment as _Environment
_Environment = _Environment
import dev.ultreon.quantum.debug.inspect.InspectionRoot as _InspectionRoot
_InspectionRoot = _InspectionRoot
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum.client import input
except ImportError:
    input = _import_once("pyquantum.client.input")

import java.lang.Integer as _int
import java.lang.Throwable as Throwable
import dev.ultreon.quantum.client.ServerData as _ServerData
_ServerData = _ServerData
try:
    from pyquantum.client import rpc
except ImportError:
    rpc = _import_once("pyquantum.client.rpc")

 
class QuantumClient():
    """dev.ultreon.quantum.client.QuantumClient"""
 
    @staticmethod
    def _wrap(java_value: _QuantumClient) -> 'QuantumClient':
        return QuantumClient(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _QuantumClient):
        """
        Dynamic initializer for QuantumClient.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_QuantumClient__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_QuantumClient__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.debug.profiler.Profiler dev.ultreon.quantum.client.QuantumClient.PROFILER
    PROFILER: 'profiler.Profiler' = _wrap(_profiler.Profiler.PROFILER)

    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.client.QuantumClient.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Callable') -> object:
        """public static <T> T dev.ultreon.quantum.client.QuantumClient.invokeAndWait(java.util.concurrent.Callable<T>)"""
        return object._wrap(_QuantumClient.invokeAndWait(arg0))

    @staticmethod
    @overload
    def ggBro() -> 'util.GG':
        """public static dev.ultreon.quantum.client.util.GG dev.ultreon.quantum.client.QuantumClient.ggBro()"""
        return util.GG._wrap(_QuantumClient.ggBro())

    @property
    def player(self, value: 'player.LocalPlayer'):
        super(_QuantumClient).player(value)

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

    @overload
    def startIntegratedServer(self):
        """public void dev.ultreon.quantum.client.QuantumClient.startIntegratedServer()"""
        super(QuantumClient, self).startIntegratedServer()

    @overload
    def getBreakProgress(self) -> float:
        """public float dev.ultreon.quantum.client.QuantumClient.getBreakProgress()"""
        return float._wrap(super(QuantumClient, self).getBreakProgress())

    @staticmethod
    @overload
    def invoke(arg0: 'Runnable') -> 'CompletableFuture':
        """public static java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.client.QuantumClient.invoke(java.lang.Runnable)"""
        return CompletableFuture._wrap(_QuantumClient.invoke(arg0))

    @property
    def motionPointer(self, value: 'input.TouchPoint'):
        super(_QuantumClient).motionPointer(value)

    @overload
    def isLoading(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isLoading()"""
        return bool._wrap(super(QuantumClient, self).isLoading())

    @property
    def hitResult(self) -> HitResult:
        return HitResult._wrap(super(_QuantumClient).hitResult())

    @override
    @overload
    def pollAll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.pollAll()"""
        super(util.PollingExecutorService, self).pollAll()

    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.QuantumClient.getWidth()"""
        return int._wrap(super(QuantumClient, self).getWidth())

    @staticmethod
    @overload
    def crash(arg0: 'CrashLog'):
        """public static void dev.ultreon.quantum.client.QuantumClient.crash(dev.ultreon.quantum.crash.CrashLog)"""
        _QuantumClient.crash(arg0)

    @overload
    def pause(self):
        """public void dev.ultreon.quantum.client.QuantumClient.pause()"""
        super(QuantumClient, self).pause()

    @property
    def entityModelManager(self) -> EntityModelRegistry:
        return EntityModelRegistry._wrap(super(_QuantumClient).entityModelManager())

    @staticmethod
    @overload
    def getIcons() -> List[str]:
        """public static java.lang.String[] dev.ultreon.quantum.client.QuantumClient.getIcons()"""
        return List[str]._wrap(_QuantumClient.getIcons())

    @overload
    def getShaderProviderManager(self) -> 'management.ShaderProviderManager':
        """public dev.ultreon.quantum.client.management.ShaderProviderManager dev.ultreon.quantum.client.QuantumClient.getShaderProviderManager()"""
        return 'management.ShaderProviderManager'._wrap(super(QuantumClient, self).getShaderProviderManager())

    @override
    @overload
    def poll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.poll()"""
        super(util.PollingExecutorService, self).poll()

    @property
    def blocksTextureAtlas(self, value: 'atlas.TextureAtlas'):
        super(_QuantumClient).blocksTextureAtlas(value)

    @property
    def integratedServer(self) -> IntegratedServer:
        return IntegratedServer._wrap(super(_QuantumClient).integratedServer())

    @overload
    def reloadResourcesAsync(self):
        """public void dev.ultreon.quantum.client.QuantumClient.reloadResourcesAsync()"""
        super(QuantumClient, self).reloadResourcesAsync()

    @property
    def newConfig(self) -> ClientConfig:
        return ClientConfig._wrap(super(_QuantumClient).newConfig())

    @property
    def camera(self) -> GameCamera:
        return GameCamera._wrap(super(_QuantumClient).camera())

    @property
    def newFont(self) -> Font:
        return Font._wrap(super(_QuantumClient).newFont())

    @overload
    def getPipeline(self) -> 'pipeline.RenderPipeline':
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline dev.ultreon.quantum.client.QuantumClient.getPipeline()"""
        return 'pipeline.RenderPipeline'._wrap(super(QuantumClient, self).getPipeline())

    @overload
    def deferClose(self, arg0: 'AutoCloseable') -> 'AutoCloseable':
        """public <T extends java.lang.AutoCloseable> T dev.ultreon.quantum.client.QuantumClient.deferClose(T)"""
        return 'AutoCloseable'._wrap(super(_QuantumClient, self).deferClose(arg0))

    @overload
    def delayDispose(self, arg0: 'Disposable'):
        """public void dev.ultreon.quantum.client.QuantumClient.delayDispose(com.badlogic.gdx.utils.Disposable)"""
        super(_QuantumClient, self).delayDispose(arg0)

    @property
    def soundRegistry(self) -> ClientSoundRegistry:
        return ClientSoundRegistry._wrap(super(_QuantumClient).soundRegistry())

    @overload
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit') -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_util.PollingExecutorService, self).awaitTermination(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def resource(arg0: 'Identifier') -> 'files.FileHandle':
        """public static com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.QuantumClient.resource(dev.ultreon.quantum.util.Identifier)"""
        return files.FileHandle._wrap(_QuantumClient.resource(arg0))

    @staticmethod
    @overload
    def strId(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.quantum.client.QuantumClient.strId(java.lang.String)"""
        return str._wrap(_QuantumClient.strId(arg0))

    @overload
    def setFullScreen(self, arg0: bool):
        """public void dev.ultreon.quantum.client.QuantumClient.setFullScreen(boolean)"""
        super(_QuantumClient, self).setFullScreen(_boolean.valueOf(arg0))

    @property
    def itemTextureAtlas(self) -> TextureAtlas:
        return TextureAtlas._wrap(super(_QuantumClient).itemTextureAtlas())

    @overload
    def fillGameInfo(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.client.QuantumClient.fillGameInfo(dev.ultreon.quantum.crash.CrashLog)"""
        super(_QuantumClient, self).fillGameInfo(arg0)

    @overload
    def isClosingWorld(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isClosingWorld()"""
        return bool._wrap(super(QuantumClient, self).isClosingWorld())

    @overload
    def screenshot(self, arg0: bool) -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<dev.ultreon.quantum.client.Screenshot> dev.ultreon.quantum.client.QuantumClient.screenshot(boolean)"""
        return 'CompletableFuture'._wrap(super(_QuantumClient, self).screenshot(_boolean.valueOf(arg0)))

    @overload
    def getModConfigScreen(self, arg0: 'Mod') -> 'config.ConfigScreenFactory':
        """public dev.ultreon.quantum.client.config.ConfigScreenFactory dev.ultreon.quantum.client.QuantumClient.getModConfigScreen(dev.ultreon.quantum.Mod)"""
        return 'config.ConfigScreenFactory'._wrap(super(_QuantumClient, self).getModConfigScreen(arg0))

    @overload
    def getMultiplayerData(self) -> 'multiplayer.MultiplayerData':
        """public dev.ultreon.quantum.client.multiplayer.MultiplayerData dev.ultreon.quantum.client.QuantumClient.getMultiplayerData()"""
        return 'multiplayer.MultiplayerData'._wrap(super(QuantumClient, self).getMultiplayerData())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Runnable'):
        """public static void dev.ultreon.quantum.client.QuantumClient.invokeAndWait(java.lang.Runnable)"""
        _QuantumClient.invokeAndWait(arg0)

    @property
    def input(self) -> GameInput:
        return GameInput._wrap(super(_QuantumClient).input())

    @property
    def metadata(self, value: 'Metadata'):
        super(_QuantumClient).metadata(value)

    @overload
    def attack(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.client.QuantumClient.attack(dev.ultreon.quantum.entity.Entity)"""
        super(_QuantumClient, self).attack(arg0)

    @overload
    def getShaderProgramManager(self) -> 'management.ShaderProgramManager':
        """public dev.ultreon.quantum.client.management.ShaderProgramManager dev.ultreon.quantum.client.QuantumClient.getShaderProgramManager()"""
        return 'management.ShaderProgramManager'._wrap(super(QuantumClient, self).getShaderProgramManager())

    @property
    def font(self) -> Font:
        return Font._wrap(super(_QuantumClient).font())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getGameVersion() -> str:
        """public static java.lang.String dev.ultreon.quantum.client.QuantumClient.getGameVersion()"""
        return str._wrap(_QuantumClient.getGameVersion())

    @overload
    def tryShutdown(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.tryShutdown()"""
        return bool._wrap(super(QuantumClient, self).tryShutdown())

    @property
    def entityRendererManager(self) -> EntityRendererRegistry:
        return EntityRendererRegistry._wrap(super(_QuantumClient).entityRendererManager())

    @overload
    def getBlockModel(self, arg0: 'BlockProperties') -> 'block.BlockModel':
        """public dev.ultreon.quantum.client.model.block.BlockModel dev.ultreon.quantum.client.QuantumClient.getBlockModel(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'block.BlockModel'._wrap(super(_QuantumClient, self).getBlockModel(arg0))

    @overload
    def pollServerTick(self):
        """public void dev.ultreon.quantum.client.QuantumClient.pollServerTick()"""
        super(QuantumClient, self).pollServerTick()

    @overload
    def getMaterialManager(self) -> 'management.MaterialManager':
        """public dev.ultreon.quantum.client.management.MaterialManager dev.ultreon.quantum.client.QuantumClient.getMaterialManager()"""
        return 'management.MaterialManager'._wrap(super(QuantumClient, self).getMaterialManager())

    @staticmethod
    @overload
    def data(arg0: str) -> 'files.FileHandle':
        """public static com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.QuantumClient.data(java.lang.String)"""
        return files.FileHandle._wrap(_QuantumClient.data(arg0))

    @overload
    def deferShutdown(self, arg0: 'Shutdownable') -> 'util.Shutdownable':
        """public <T extends dev.ultreon.quantum.util.Shutdownable> T dev.ultreon.quantum.client.QuantumClient.deferShutdown(T)"""
        return 'util.Shutdownable'._wrap(super(_QuantumClient, self).deferShutdown(arg0))

    @property
    def motionPointer(self) -> TouchPoint:
        return TouchPoint._wrap(super(_QuantumClient).motionPointer())

    @overload
    def startBreaking(self):
        """public void dev.ultreon.quantum.client.QuantumClient.startBreaking()"""
        super(QuantumClient, self).startBreaking()

    @property
    def clipboard(self) -> IClipboard:
        return IClipboard._wrap(super(_QuantumClient).clipboard())

    @overload
    def filesDropped(self, arg0: 'String') -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.filesDropped(java.lang.String[])"""
        return bool._wrap(super(_QuantumClient, self).filesDropped(arg0))

    @property
    def hitResult(self, value: 'util.HitResult'):
        super(_QuantumClient).hitResult(value)

    @property
    def playerInput(self) -> PlayerInput:
        return PlayerInput._wrap(super(_QuantumClient).playerInput())

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isShutdown()"""
        return bool._wrap(super(util.PollingExecutorService, self).isShutdown())

    @overload
    def isRenderingWorld(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isRenderingWorld()"""
        return bool._wrap(super(QuantumClient, self).isRenderingWorld())

    @staticmethod
    @overload
    def get() -> 'QuantumClient':
        """public static dev.ultreon.quantum.client.QuantumClient dev.ultreon.quantum.client.QuantumClient.get()"""
        return QuantumClient._wrap(_QuantumClient.get())

    @overload
    def invokeAny(self, arg0: 'Collection') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_util.PollingExecutorService, self).invokeAny(arg0))

    @overload
    def setShowDebugHud(self, arg0: bool):
        """public void dev.ultreon.quantum.client.QuantumClient.setShowDebugHud(boolean)"""
        super(_QuantumClient, self).setShowDebugHud(_boolean.valueOf(arg0))

    @property
    def blocksTextureAtlas(self) -> TextureAtlas:
        return TextureAtlas._wrap(super(_QuantumClient).blocksTextureAtlas())

    @overload
    def getCurrentTps(self) -> int:
        """public int dev.ultreon.quantum.client.QuantumClient.getCurrentTps()"""
        return int._wrap(super(QuantumClient, self).getCurrentTps())

    @overload
    def setAutomaticScale(self, arg0: bool):
        """public void dev.ultreon.quantum.client.QuantumClient.setAutomaticScale(boolean)"""
        super(_QuantumClient, self).setAutomaticScale(_boolean.valueOf(arg0))

    @overload
    def reloadResources(self):
        """public void dev.ultreon.quantum.client.QuantumClient.reloadResources()"""
        super(QuantumClient, self).reloadResources()

    @property
    def itemTextureAtlas(self, value: 'atlas.TextureAtlas'):
        super(_QuantumClient).itemTextureAtlas(value)

    @overload
    def cyclePlayerView(self):
        """public void dev.ultreon.quantum.client.QuantumClient.cyclePlayerView()"""
        super(QuantumClient, self).cyclePlayerView()

    @overload
    def schedule(self, arg0: 'Task', arg1: int) -> 'ScheduledFuture':
        """public java.util.concurrent.ScheduledFuture<java.lang.Void> dev.ultreon.quantum.client.QuantumClient.schedule(dev.ultreon.quantum.util.Task<?>,long)"""
        return 'ScheduledFuture'._wrap(super(_QuantumClient, self).schedule(arg0, _long.valueOf(arg1)))

    @overload
    def isInThirdPerson(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isInThirdPerson()"""
        return bool._wrap(super(QuantumClient, self).isInThirdPerson())

    @property
    def inspection(self, value: 'inspect.InspectionRoot'):
        super(_QuantumClient).inspection(value)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void dev.ultreon.quantum.client.QuantumClient.main(java.lang.String[])"""
        _QuantumClient.main(arg0)

    @overload
    def getAssetManager(self) -> 'assets.AssetManager':
        """public com.badlogic.gdx.assets.AssetManager dev.ultreon.quantum.client.QuantumClient.getAssetManager()"""
        return 'assets.AssetManager'._wrap(super(QuantumClient, self).getAssetManager())

    @overload
    def getSkinManager(self) -> 'player.SkinManager':
        """public dev.ultreon.quantum.client.player.SkinManager dev.ultreon.quantum.client.QuantumClient.getSkinManager()"""
        return 'player.SkinManager'._wrap(super(QuantumClient, self).getSkinManager())

    @overload
    def exitWorldToTitle(self):
        """public void dev.ultreon.quantum.client.QuantumClient.exitWorldToTitle()"""
        super(QuantumClient, self).exitWorldToTitle()

    @property
    def world(self, value: 'world.ClientWorld'):
        super(_QuantumClient).world(value)

    @overload
    def submit(self, arg0: 'Runnable', arg1: object) -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable,T)"""
        return 'CompletableFuture'._wrap(super(_util.PollingExecutorService, self).submit(arg0, arg1))

    @overload
    def runInTick(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.client.QuantumClient.runInTick(java.lang.Runnable)"""
        super(_QuantumClient, self).runInTick(arg0)

    @property
    def worldRenderer(self, value: 'world.WorldRenderer'):
        super(_QuantumClient).worldRenderer(value)

    @overload
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_util.PollingExecutorService, self).invokeAny(arg0, _long.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def getGameDir() -> 'Path':
        """public static java.nio.file.Path dev.ultreon.quantum.client.QuantumClient.getGameDir()"""
        return Path._wrap(_QuantumClient.getGameDir())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def connectToServer(self, arg0: str, arg1: int):
        """public void dev.ultreon.quantum.client.QuantumClient.connectToServer(java.lang.String,int)"""
        super(_QuantumClient, self).connectToServer(arg0, _int.valueOf(arg1))

    @property
    def integratedServer(self, value: 'IntegratedServer'):
        super(_QuantumClient).integratedServer(value)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.QuantumClient.toString()"""
        return str._wrap(super(QuantumClient, self).toString())

    @overload
    def isPlaying(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isPlaying()"""
        return bool._wrap(super(QuantumClient, self).isPlaying())

    @overload
    def deferDispose(self, arg0: 'Disposable') -> 'utils.Disposable':
        """public <T extends com.badlogic.gdx.utils.Disposable> T dev.ultreon.quantum.client.QuantumClient.deferDispose(T)"""
        return 'utils.Disposable'._wrap(super(_QuantumClient, self).deferDispose(arg0))

    @property
    def emmisiveTextureAtlas(self, value: 'atlas.TextureAtlas'):
        super(_QuantumClient).emmisiveTextureAtlas(value)

    @overload
    def render(self):
        """public void dev.ultreon.quantum.client.QuantumClient.render()"""
        super(QuantumClient, self).render()

    @overload
    def clientTick(self):
        """public void dev.ultreon.quantum.client.QuantumClient.clientTick()"""
        super(QuantumClient, self).clientTick()

    @property
    def screen(self, value: 'gui.Screen'):
        super(_QuantumClient).screen(value)

    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.QuantumClient.getHeight()"""
        return int._wrap(super(QuantumClient, self).getHeight())

    @overload
    def isShowDebugHud(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isShowDebugHud()"""
        return bool._wrap(super(QuantumClient, self).isShowDebugHud())

    @overload
    def delayCrash(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.client.QuantumClient.delayCrash(dev.ultreon.quantum.crash.CrashLog)"""
        super(_QuantumClient, self).delayCrash(arg0)

    @property
    def player(self) -> LocalPlayer:
        return LocalPlayer._wrap(super(_QuantumClient).player())

    @staticmethod
    @overload
    def setCrashHook(arg0: 'Callback'):
        """public static void dev.ultreon.quantum.client.QuantumClient.setCrashHook(dev.ultreon.quantum.client.gui.Callback<dev.ultreon.quantum.crash.CrashLog>)"""
        _QuantumClient.setCrashHook(arg0)

    @overload
    def setInThirdPerson(self, arg0: bool):
        """public void dev.ultreon.quantum.client.QuantumClient.setInThirdPerson(boolean)"""
        super(_QuantumClient, self).setInThirdPerson(_boolean.valueOf(arg0))

    @overload
    def getEnvironment(self) -> 'g3d.Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment dev.ultreon.quantum.client.QuantumClient.getEnvironment()"""
        return 'g3d.Environment'._wrap(super(QuantumClient, self).getEnvironment())

    @property
    def metadata(self) -> Metadata:
        return Metadata._wrap(super(_QuantumClient).metadata())

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
    def isTerminated(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isTerminated()"""
        return bool._wrap(super(util.PollingExecutorService, self).isTerminated())

    @property
    def openedWorld(self, value: 'world.WorldStorage'):
        super(_QuantumClient).openedWorld(value)

    @override
    @overload
    def close(self):
        """public default void java.util.concurrent.ExecutorService.close()"""
        super(ExecutorService, self).close()

    @overload
    def getResourceManager(self) -> 'resources.ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.client.QuantumClient.getResourceManager()"""
        return 'resources.ResourceManager'._wrap(super(QuantumClient, self).getResourceManager())

    @staticmethod
    @overload
    def isOnMainThread() -> bool:
        """public static boolean dev.ultreon.quantum.client.QuantumClient.isOnMainThread()"""
        return bool._wrap(_QuantumClient.isOnMainThread())

    @overload
    def resetBreaking(self):
        """public void dev.ultreon.quantum.client.QuantumClient.resetBreaking()"""
        super(QuantumClient, self).resetBreaking()

    @property
    def hud(self) -> Hud:
        return Hud._wrap(super(_QuantumClient).hud())

    @overload
    def addFuture(self, arg0: 'CompletableFuture'):
        """public void dev.ultreon.quantum.client.QuantumClient.addFuture(java.util.concurrent.CompletableFuture<?>)"""
        super(_QuantumClient, self).addFuture(arg0)

    @overload
    def getPlayerView(self) -> 'util.PlayerView':
        """public dev.ultreon.quantum.client.util.PlayerView dev.ultreon.quantum.client.QuantumClient.getPlayerView()"""
        return 'util.PlayerView'._wrap(super(QuantumClient, self).getPlayerView())

    @property
    def debugGui(self, value: 'debug.DebugOverlay'):
        super(_QuantumClient).debugGui(value)

    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.QuantumClient.resize(int,int)"""
        super(_QuantumClient, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def startWorld(self, arg0: 'WorldStorage'):
        """public void dev.ultreon.quantum.client.QuantumClient.startWorld(dev.ultreon.quantum.world.WorldStorage)"""
        super(_QuantumClient, self).startWorld(arg0)

    @staticmethod
    @overload
    def crash(arg0: 'Throwable'):
        """public static void dev.ultreon.quantum.client.QuantumClient.crash(java.lang.Throwable)"""
        _QuantumClient.crash(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @property
    def hud(self, value: 'gui.Hud'):
        super(_QuantumClient).hud(value)

    @overload
    def schedule(self, arg0: 'Task', arg1: int, arg2: 'TimeUnit') -> 'ScheduledFuture':
        """public java.util.concurrent.ScheduledFuture<java.lang.Void> dev.ultreon.quantum.client.QuantumClient.schedule(dev.ultreon.quantum.util.Task<?>,long,java.util.concurrent.TimeUnit)"""
        return 'ScheduledFuture'._wrap(super(_QuantumClient, self).schedule(arg0, _long.valueOf(arg1), arg2))

        @staticmethod
        @overload
        def logDebug():
            """public static void dev.ultreon.quantum.client.QuantumClient.logDebug()"""
            _QuantumClient.logDebug()

    @property
    def serverData(self) -> ServerData:
        return ServerData._wrap(super(_QuantumClient).serverData())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.QuantumClient.dispose()"""
        super(QuantumClient, self).dispose()

    @overload
    def setPlayerView(self, arg0: 'PlayerView'):
        """public void dev.ultreon.quantum.client.QuantumClient.setPlayerView(dev.ultreon.quantum.client.util.PlayerView)"""
        super(_QuantumClient, self).setPlayerView(arg0)

    @property
    def settings(self) -> GameSettings:
        return GameSettings._wrap(super(_QuantumClient).settings())

    @property
    def profiler(self) -> Profiler:
        return Profiler._wrap(super(_PollingExecutorService).profiler())

    @staticmethod
    @overload
    def getConfigDir() -> 'files.FileHandle':
        """public static com.badlogic.gdx.files.FileHandle dev.ultreon.quantum.client.QuantumClient.getConfigDir()"""
        return files.FileHandle._wrap(_QuantumClient.getConfigDir())

    @property
    def connection(self) -> IConnection:
        return IConnection._wrap(super(_QuantumClient).connection())

    @overload
    def setGuiScale(self, arg0: float):
        """public void dev.ultreon.quantum.client.QuantumClient.setGuiScale(float)"""
        super(_QuantumClient, self).setGuiScale(_float.valueOf(arg0))

    @staticmethod
    @overload
    def isPackaged() -> bool:
        """public static boolean dev.ultreon.quantum.client.QuantumClient.isPackaged()"""
        return bool._wrap(_QuantumClient.isPackaged())

    @overload
    def getSingleplayerServer(self) -> 'IntegratedServer':
        """public dev.ultreon.quantum.client.IntegratedServer dev.ultreon.quantum.client.QuantumClient.getSingleplayerServer()"""
        return 'IntegratedServer'._wrap(super(QuantumClient, self).getSingleplayerServer())

    @overload
    def getScaledWidth(self) -> int:
        """public int dev.ultreon.quantum.client.QuantumClient.getScaledWidth()"""
        return int._wrap(super(QuantumClient, self).getScaledWidth())

    @overload
    def invokeAll(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit)"""
        return 'List'._wrap(super(_util.PollingExecutorService, self).invokeAll(arg0, _long.valueOf(arg1), arg2))

    @property
    def openedWorld(self) -> WorldStorage:
        return WorldStorage._wrap(super(_QuantumClient).openedWorld())

    @property
    def cursor(self, value: 'util.BlockHitResult'):
        super(_QuantumClient).cursor(value)

    @overload
    def resume(self):
        """public void dev.ultreon.quantum.client.QuantumClient.resume()"""
        super(QuantumClient, self).resume()

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> dev.ultreon.quantum.util.PollingExecutorService.shutdownNow()"""
        return 'List'._wrap(super(util.PollingExecutorService, self).shutdownNow())

    @staticmethod
    @overload
    def id(arg0: str) -> 'util.Identifier':
        """public static dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.QuantumClient.id(java.lang.String)"""
        return util.Identifier._wrap(_QuantumClient.id(arg0))

    @property
    def cursor(self) -> BlockHitResult:
        return BlockHitResult._wrap(super(_QuantumClient).cursor())

    @staticmethod
    @overload
    def interpolate(arg0: float, arg1: float, arg2: float) -> float:
        """public static double dev.ultreon.quantum.client.QuantumClient.interpolate(double,double,double)"""
        return float._wrap(_QuantumClient.interpolate(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def isSinglePlayer(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isSinglePlayer()"""
        return bool._wrap(super(QuantumClient, self).isSinglePlayer())

    @overload
    def invokeAll(self, arg0: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>)"""
        return 'List'._wrap(super(_util.PollingExecutorService, self).invokeAll(arg0))

    @overload
    def playSound(self, arg0: 'SoundEvent', arg1: float):
        """public void dev.ultreon.quantum.client.QuantumClient.playSound(dev.ultreon.quantum.world.SoundEvent,float)"""
        super(_QuantumClient, self).playSound(arg0, _float.valueOf(arg1))

    @overload
    def startDevWorld(self):
        """public void dev.ultreon.quantum.client.QuantumClient.startDevWorld()"""
        super(QuantumClient, self).startDevWorld()

    @staticmethod
    @overload
    def setFpsLimit(arg0: int):
        """public static void dev.ultreon.quantum.client.QuantumClient.setFpsLimit(int)"""
        _QuantumClient.setFpsLimit(_int.valueOf(arg0))

    @property
    def settings(self, value: 'config.GameSettings'):
        super(_QuantumClient).settings(value)

    @overload
    def getScaledHeight(self) -> int:
        """public int dev.ultreon.quantum.client.QuantumClient.getScaledHeight()"""
        return int._wrap(super(QuantumClient, self).getScaledHeight())

    @staticmethod
    @overload
    def getGameEnv() -> 'GameEnvironment':
        """public static dev.ultreon.quantum.client.GameEnvironment dev.ultreon.quantum.client.QuantumClient.getGameEnv()"""
        return GameEnvironment._wrap(_QuantumClient.getGameEnv())

    @overload
    def setActivity(self, arg0: 'GameActivity'):
        """public void dev.ultreon.quantum.client.QuantumClient.setActivity(dev.ultreon.quantum.client.rpc.GameActivity)"""
        super(_QuantumClient, self).setActivity(arg0)

    @overload
    def submit(self, arg0: 'Callable') -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'CompletableFuture'._wrap(super(_util.PollingExecutorService, self).submit(arg0))

    @property
    def renderer(self) -> Renderer:
        return Renderer._wrap(super(_QuantumClient).renderer())

    @property
    def emmisiveTextureAtlas(self) -> TextureAtlas:
        return TextureAtlas._wrap(super(_QuantumClient).emmisiveTextureAtlas())

    @overload
    def setModConfigScreen(self, arg0: 'Mod', arg1: 'ConfigScreenFactory'):
        """public void dev.ultreon.quantum.client.QuantumClient.setModConfigScreen(dev.ultreon.quantum.Mod,dev.ultreon.quantum.client.config.ConfigScreenFactory)"""
        super(_QuantumClient, self).setModConfigScreen(arg0, arg1)

    @property
    def input(self, value: 'input.GameInput'):
        super(_QuantumClient).input(value)

    @override
    @overload
    def execute(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.util.PollingExecutorService.execute(java.lang.Runnable)"""
        super(_util.PollingExecutorService, self).execute(arg0)

    @overload
    def setShowingImGui(self, arg0: bool):
        """public void dev.ultreon.quantum.client.QuantumClient.setShowingImGui(boolean)"""
        super(_QuantumClient, self).setShowingImGui(_boolean.valueOf(arg0))

    @overload
    def exitWorldAndThen(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.client.QuantumClient.exitWorldAndThen(java.lang.Runnable)"""
        super(_QuantumClient, self).exitWorldAndThen(arg0)

    @overload
    def getWindow(self) -> 'pyquantum.GameWindow':
        """public dev.ultreon.quantum.GameWindow dev.ultreon.quantum.client.QuantumClient.getWindow()"""
        return 'pyquantum.GameWindow'._wrap(super(QuantumClient, self).getWindow())

    @overload
    def getBootTime(self) -> 'v0.Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.quantum.client.QuantumClient.getBootTime()"""
        return 'v0.Duration'._wrap(super(QuantumClient, self).getBootTime())

    @overload
    def getDrawOffset(self) -> 'math.GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 dev.ultreon.quantum.client.QuantumClient.getDrawOffset()"""
        return 'math.GridPoint2'._wrap(super(QuantumClient, self).getDrawOffset())

    @overload
    def getTextureManager(self) -> 'texture.TextureManager':
        """public dev.ultreon.quantum.client.texture.TextureManager dev.ultreon.quantum.client.QuantumClient.getTextureManager()"""
        return 'texture.TextureManager'._wrap(super(QuantumClient, self).getTextureManager())

    @overload
    def isShowingImGui(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isShowingImGui()"""
        return bool._wrap(super(QuantumClient, self).isShowingImGui())

    @overload
    def isFullScreen(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isFullScreen()"""
        return bool._wrap(super(QuantumClient, self).isFullScreen())

    @property
    def itemRenderer(self) -> ItemRenderer:
        return ItemRenderer._wrap(super(_QuantumClient).itemRenderer())

    @staticmethod
    @overload
    def invoke(arg0: 'Callable') -> 'CompletableFuture':
        """public static <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.client.QuantumClient.invoke(java.util.concurrent.Callable<T>)"""
        return CompletableFuture._wrap(_QuantumClient.invoke(arg0))

    @property
    def connection(self, value: 'system.IConnection'):
        super(_QuantumClient).connection(value)

    @overload
    def isDevMode(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isDevMode()"""
        return bool._wrap(super(QuantumClient, self).isDevMode())

    @property
    def itemRenderer(self, value: 'item.ItemRenderer'):
        super(_QuantumClient).itemRenderer(value)

    @property
    def serverData(self, value: 'ServerData'):
        super(_QuantumClient).serverData(value)

    @property
    def newConfig(self, value: 'config.ClientConfig'):
        super(_QuantumClient).newConfig(value)

    @overload
    def stopBreaking(self):
        """public void dev.ultreon.quantum.client.QuantumClient.stopBreaking()"""
        super(QuantumClient, self).stopBreaking()

    @overload
    def showScreen(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.showScreen(dev.ultreon.quantum.client.gui.Screen)"""
        return bool._wrap(super(_QuantumClient, self).showScreen(arg0))

    @overload
    def getGuiScale(self) -> float:
        """public float dev.ultreon.quantum.client.QuantumClient.getGuiScale()"""
        return float._wrap(super(QuantumClient, self).getGuiScale())

    @property
    def inspection(self) -> InspectionRoot:
        return InspectionRoot._wrap(super(_QuantumClient).inspection())

    @property
    def debugGui(self) -> DebugOverlay:
        return DebugOverlay._wrap(super(_QuantumClient).debugGui())

    @overload
    def onDisconnect(self, arg0: str):
        """public void dev.ultreon.quantum.client.QuantumClient.onDisconnect(java.lang.String)"""
        super(_QuantumClient, self).onDisconnect(arg0)

    @property
    def notifications(self) -> NotifyManager:
        return NotifyManager._wrap(super(_QuantumClient).notifications())

    @overload
    def playSound(self, arg0: 'ClientSound'):
        """public void dev.ultreon.quantum.client.QuantumClient.playSound(dev.ultreon.quantum.client.audio.ClientSound)"""
        super(_QuantumClient, self).playSound(arg0)

    @overload
    def submit(self, arg0: 'Runnable') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable)"""
        return 'CompletableFuture'._wrap(super(_util.PollingExecutorService, self).submit(arg0))

    @overload
    def isCustomBorderShown(self) -> bool:
        """public boolean dev.ultreon.quantum.client.QuantumClient.isCustomBorderShown()"""
        return bool._wrap(super(QuantumClient, self).isCustomBorderShown())

    @property
    def notifications(self, value: 'gui.NotifyManager'):
        super(_QuantumClient).notifications(value)

    @overload
    def startWorld(self, arg0: 'Path'):
        """public void dev.ultreon.quantum.client.QuantumClient.startWorld(java.nio.file.Path)"""
        super(_QuantumClient, self).startWorld(arg0)

    @overload
    def screenshot(self) -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<dev.ultreon.quantum.client.Screenshot> dev.ultreon.quantum.client.QuantumClient.screenshot()"""
        return 'CompletableFuture'._wrap(super(QuantumClient, self).screenshot())

    @property
    def worldRenderer(self) -> WorldRenderer:
        return WorldRenderer._wrap(super(_QuantumClient).worldRenderer())

    @property
    def world(self) -> ClientWorld:
        return ClientWorld._wrap(super(_QuantumClient).world())

    @property
    def screen(self) -> Screen:
        return Screen._wrap(super(_QuantumClient).screen())

    @overload
    def getUser(self) -> 'User':
        """public dev.ultreon.quantum.client.User dev.ultreon.quantum.client.QuantumClient.getUser()"""
        return 'User'._wrap(super(QuantumClient, self).getUser()) 
 
 
# CLASS: dev.ultreon.quantum.client.Constants
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import dev.ultreon.quantum.client.Constants as _Constants
_Constants = _Constants
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Constants():
    """dev.ultreon.quantum.client.Constants"""
 
    @staticmethod
    def _wrap(java_value: _Constants) -> 'Constants':
        return Constants(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Constants):
        """
        Dynamic initializer for Constants.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Constants__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Constants__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.Constants()"""
        val = _Constants()
        self.__wrapper = val

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.Constants()"""
        val = _Constants()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.RenderingRegistration
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.RenderingRegistration as _RenderingRegistration
_RenderingRegistration = _RenderingRegistration
import java.lang.String as _String
_String = _String
try:
    from pyquantum.client import registry
except ImportError:
    registry = _import_once("pyquantum.client.registry")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RenderingRegistration():
    """dev.ultreon.quantum.client.RenderingRegistration"""
 
    @staticmethod
    def _wrap(java_value: _RenderingRegistration) -> 'RenderingRegistration':
        return RenderingRegistration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderingRegistration):
        """
        Dynamic initializer for RenderingRegistration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderingRegistration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderingRegistration__wrapper":
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
    def registerRendering(arg0: 'QuantumClient'):
        """public static void dev.ultreon.quantum.client.RenderingRegistration.registerRendering(dev.ultreon.quantum.client.QuantumClient)"""
        _RenderingRegistration.registerRendering(arg0)

    @staticmethod
    @overload
    def registerEntityRendering(arg0: 'EntityModelRegistry'):
        """public static void dev.ultreon.quantum.client.RenderingRegistration.registerEntityRendering(dev.ultreon.quantum.client.registry.EntityModelRegistry)"""
        _RenderingRegistration.registerEntityRendering(arg0)

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
        def registerEntityRenderers():
            """public static void dev.ultreon.quantum.client.RenderingRegistration.registerEntityRenderers()"""
            _RenderingRegistration.registerEntityRenderers()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.RenderingRegistration()"""
        val = _RenderingRegistration()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.RenderingRegistration()"""
        val = _RenderingRegistration()
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