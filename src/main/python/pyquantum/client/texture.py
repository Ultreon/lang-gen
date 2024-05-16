from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.resources.ResourceManager as __ResourceManager
__ResourceManager = __ResourceManager
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.texture.TextureManager as __TextureManager
__TextureManager = __TextureManager
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
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class TextureManager():
    """dev.ultreon.quantum.client.texture.TextureManager"""
 
    @staticmethod
    def __wrap(java_value: __TextureManager) -> 'TextureManager':
        return TextureManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureManager):
        """
        Dynamic initializer for TextureManager.
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
    def registerTexture(self, arg0: 'Identifier') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.registerTexture(dev.ultreon.quantum.util.Identifier)"""
        return 'graphics.Texture'.__wrap(super(__TextureManager, self).registerTexture(arg0))

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
    def getTexture(self, arg0: 'Identifier', arg1: 'Texture') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.getTexture(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture)"""
        return 'graphics.Texture'.__wrap(super(__TextureManager, self).getTexture(arg0, arg1))

    @overload
    def getTexture(self, arg0: 'Identifier') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.getTexture(dev.ultreon.quantum.util.Identifier)"""
        return 'graphics.Texture'.__wrap(super(__TextureManager, self).getTexture(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.texture.TextureManager.dispose()"""
        super(TextureManager, self).dispose()

    @overload
    def registerTexture(self, arg0: 'Identifier', arg1: 'Texture') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.registerTexture(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture)"""
        return 'graphics.Texture'.__wrap(super(__TextureManager, self).registerTexture(arg0, arg1))

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
    def __init__(self, arg0: 'ResourceManager'):
        """public dev.ultreon.quantum.client.texture.TextureManager(dev.ultreon.quantum.resources.ResourceManager)"""
        val = __TextureManager(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getResourceManager(self) -> 'resources.ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.client.texture.TextureManager.getResourceManager()"""
        return 'resources.ResourceManager'.__wrap(super(TextureManager, self).getResourceManager())

    @overload
    def isTextureLoaded(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.client.texture.TextureManager.isTextureLoaded(dev.ultreon.quantum.util.Identifier)"""
        return bool.__wrap(super(__TextureManager, self).isTextureLoaded(arg0))

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
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.texture.TextureManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(__TextureManager, self).reload(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def registerTextureFB(self, arg0: 'Identifier', arg1: 'Texture') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.registerTextureFB(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture)"""
        return 'graphics.Texture'.__wrap(super(__TextureManager, self).registerTextureFB(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.texture.TextureManager
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.resources.ResourceManager as __ResourceManager
__ResourceManager = __ResourceManager
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.texture.TextureManager as __TextureManager
__TextureManager = __TextureManager
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
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class TextureManager():
    """dev.ultreon.quantum.client.texture.TextureManager"""
 
    @staticmethod
    def __wrap(java_value: __TextureManager) -> 'TextureManager':
        return TextureManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureManager):
        """
        Dynamic initializer for TextureManager.
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
    def registerTexture(self, arg0: 'Identifier') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.registerTexture(dev.ultreon.quantum.util.Identifier)"""
        return 'graphics.Texture'.__wrap(super(__TextureManager, self).registerTexture(arg0))

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
    def getTexture(self, arg0: 'Identifier', arg1: 'Texture') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.getTexture(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture)"""
        return 'graphics.Texture'.__wrap(super(__TextureManager, self).getTexture(arg0, arg1))

    @overload
    def getTexture(self, arg0: 'Identifier') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.getTexture(dev.ultreon.quantum.util.Identifier)"""
        return 'graphics.Texture'.__wrap(super(__TextureManager, self).getTexture(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.texture.TextureManager.dispose()"""
        super(TextureManager, self).dispose()

    @overload
    def registerTexture(self, arg0: 'Identifier', arg1: 'Texture') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.registerTexture(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture)"""
        return 'graphics.Texture'.__wrap(super(__TextureManager, self).registerTexture(arg0, arg1))

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
    def __init__(self, arg0: 'ResourceManager'):
        """public dev.ultreon.quantum.client.texture.TextureManager(dev.ultreon.quantum.resources.ResourceManager)"""
        val = __TextureManager(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getResourceManager(self) -> 'resources.ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.client.texture.TextureManager.getResourceManager()"""
        return 'resources.ResourceManager'.__wrap(super(TextureManager, self).getResourceManager())

    @overload
    def isTextureLoaded(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.client.texture.TextureManager.isTextureLoaded(dev.ultreon.quantum.util.Identifier)"""
        return bool.__wrap(super(__TextureManager, self).isTextureLoaded(arg0))

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
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.texture.TextureManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(__TextureManager, self).reload(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def registerTextureFB(self, arg0: 'Identifier', arg1: 'Texture') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.registerTextureFB(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture)"""
        return 'graphics.Texture'.__wrap(super(__TextureManager, self).registerTextureFB(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.texture.TextureManager