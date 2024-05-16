from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.client.texture.TextureManager as _TextureManager
_TextureManager = _TextureManager
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.resources.ResourceManager as _ResourceManager
_ResourceManager = _ResourceManager
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureManager():
    """dev.ultreon.quantum.client.texture.TextureManager"""
 
    @staticmethod
    def _wrap(java_value: _TextureManager) -> 'TextureManager':
        return TextureManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureManager):
        """
        Dynamic initializer for TextureManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureManager__wrapper":
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

    @overload
    def __init__(self, arg0: 'ResourceManager'):
        """public dev.ultreon.quantum.client.texture.TextureManager(dev.ultreon.quantum.resources.ResourceManager)"""
        val = _TextureManager(arg0)
        self.__wrapper = val

    @overload
    def getTexture(self, arg0: 'Identifier') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.getTexture(dev.ultreon.quantum.util.Identifier)"""
        return 'graphics.Texture'._wrap(super(_TextureManager, self).getTexture(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.texture.TextureManager.dispose()"""
        super(TextureManager, self).dispose()

    @overload
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.texture.TextureManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(_TextureManager, self).reload(arg0)

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
    def getTexture(self, arg0: 'Identifier', arg1: 'Texture') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.getTexture(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture)"""
        return 'graphics.Texture'._wrap(super(_TextureManager, self).getTexture(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def registerTexture(self, arg0: 'Identifier', arg1: 'Texture') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.registerTexture(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture)"""
        return 'graphics.Texture'._wrap(super(_TextureManager, self).registerTexture(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getResourceManager(self) -> 'resources.ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.client.texture.TextureManager.getResourceManager()"""
        return 'resources.ResourceManager'._wrap(super(TextureManager, self).getResourceManager())

    @overload
    def isTextureLoaded(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.client.texture.TextureManager.isTextureLoaded(dev.ultreon.quantum.util.Identifier)"""
        return bool._wrap(super(_TextureManager, self).isTextureLoaded(arg0))

    @overload
    def registerTextureFB(self, arg0: 'Identifier', arg1: 'Texture') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.registerTextureFB(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture)"""
        return 'graphics.Texture'._wrap(super(_TextureManager, self).registerTextureFB(arg0, arg1))

    @overload
    def registerTexture(self, arg0: 'Identifier') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.registerTexture(dev.ultreon.quantum.util.Identifier)"""
        return 'graphics.Texture'._wrap(super(_TextureManager, self).registerTexture(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.texture.TextureManager
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.client.texture.TextureManager as _TextureManager
_TextureManager = _TextureManager
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.resources.ResourceManager as _ResourceManager
_ResourceManager = _ResourceManager
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureManager():
    """dev.ultreon.quantum.client.texture.TextureManager"""
 
    @staticmethod
    def _wrap(java_value: _TextureManager) -> 'TextureManager':
        return TextureManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureManager):
        """
        Dynamic initializer for TextureManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureManager__wrapper":
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

    @overload
    def __init__(self, arg0: 'ResourceManager'):
        """public dev.ultreon.quantum.client.texture.TextureManager(dev.ultreon.quantum.resources.ResourceManager)"""
        val = _TextureManager(arg0)
        self.__wrapper = val

    @overload
    def getTexture(self, arg0: 'Identifier') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.getTexture(dev.ultreon.quantum.util.Identifier)"""
        return 'graphics.Texture'._wrap(super(_TextureManager, self).getTexture(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.texture.TextureManager.dispose()"""
        super(TextureManager, self).dispose()

    @overload
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.texture.TextureManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(_TextureManager, self).reload(arg0)

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
    def getTexture(self, arg0: 'Identifier', arg1: 'Texture') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.getTexture(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture)"""
        return 'graphics.Texture'._wrap(super(_TextureManager, self).getTexture(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def registerTexture(self, arg0: 'Identifier', arg1: 'Texture') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.registerTexture(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture)"""
        return 'graphics.Texture'._wrap(super(_TextureManager, self).registerTexture(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getResourceManager(self) -> 'resources.ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.client.texture.TextureManager.getResourceManager()"""
        return 'resources.ResourceManager'._wrap(super(TextureManager, self).getResourceManager())

    @overload
    def isTextureLoaded(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.client.texture.TextureManager.isTextureLoaded(dev.ultreon.quantum.util.Identifier)"""
        return bool._wrap(super(_TextureManager, self).isTextureLoaded(arg0))

    @overload
    def registerTextureFB(self, arg0: 'Identifier', arg1: 'Texture') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.registerTextureFB(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture)"""
        return 'graphics.Texture'._wrap(super(_TextureManager, self).registerTextureFB(arg0, arg1))

    @overload
    def registerTexture(self, arg0: 'Identifier') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.texture.TextureManager.registerTexture(dev.ultreon.quantum.util.Identifier)"""
        return 'graphics.Texture'._wrap(super(_TextureManager, self).registerTexture(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.texture.TextureManager