from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.client.management.Manager as _Manager
_Manager = _Manager
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client import atlas
except ImportError:
    atlas = _import_once("pyquantum.client.atlas")

try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import dev.ultreon.quantum.client.management.TextureAtlasManager as _TextureAtlasManager
_TextureAtlasManager = _TextureAtlasManager
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.client.atlas.TextureAtlas as _TextureAtlas
_TextureAtlas = _TextureAtlas
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
 
class TextureAtlasManager():
    """dev.ultreon.quantum.client.management.TextureAtlasManager"""
 
    @staticmethod
    def _wrap(java_value: _TextureAtlasManager) -> 'TextureAtlasManager':
        return TextureAtlasManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureAtlasManager):
        """
        Dynamic initializer for TextureAtlasManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureAtlasManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureAtlasManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self, arg0: 'Identifier') -> 'atlas.TextureAtlas':
        """public dev.ultreon.quantum.client.atlas.TextureAtlas dev.ultreon.quantum.client.management.TextureAtlasManager.get(dev.ultreon.quantum.util.Identifier)"""
        return 'atlas.TextureAtlas'._wrap(super(_TextureAtlasManager, self).get(arg0))

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
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.management.TextureAtlasManager(dev.ultreon.quantum.client.QuantumClient)"""
        val = _TextureAtlasManager(arg0)
        self.__wrapper = val

    @overload
    def register(self, arg0: 'Identifier', arg1: 'TextureAtlas') -> 'atlas.TextureAtlas':
        """public dev.ultreon.quantum.client.atlas.TextureAtlas dev.ultreon.quantum.client.management.TextureAtlasManager.register(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.atlas.TextureAtlas)"""
        return 'atlas.TextureAtlas'._wrap(super(_TextureAtlasManager, self).register(arg0, arg1))

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(_Manager, self).reload(arg0, arg1)

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
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.management.TextureAtlasManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(_TextureAtlasManager, self).reload(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.management.TextureAtlasManager
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.client.management.Manager as _Manager
_Manager = _Manager
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.client import atlas
except ImportError:
    atlas = _import_once("pyquantum.client.atlas")

try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import dev.ultreon.quantum.client.management.TextureAtlasManager as _TextureAtlasManager
_TextureAtlasManager = _TextureAtlasManager
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.client.atlas.TextureAtlas as _TextureAtlas
_TextureAtlas = _TextureAtlas
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
 
class TextureAtlasManager():
    """dev.ultreon.quantum.client.management.TextureAtlasManager"""
 
    @staticmethod
    def _wrap(java_value: _TextureAtlasManager) -> 'TextureAtlasManager':
        return TextureAtlasManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureAtlasManager):
        """
        Dynamic initializer for TextureAtlasManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureAtlasManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureAtlasManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self, arg0: 'Identifier') -> 'atlas.TextureAtlas':
        """public dev.ultreon.quantum.client.atlas.TextureAtlas dev.ultreon.quantum.client.management.TextureAtlasManager.get(dev.ultreon.quantum.util.Identifier)"""
        return 'atlas.TextureAtlas'._wrap(super(_TextureAtlasManager, self).get(arg0))

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
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.management.TextureAtlasManager(dev.ultreon.quantum.client.QuantumClient)"""
        val = _TextureAtlasManager(arg0)
        self.__wrapper = val

    @overload
    def register(self, arg0: 'Identifier', arg1: 'TextureAtlas') -> 'atlas.TextureAtlas':
        """public dev.ultreon.quantum.client.atlas.TextureAtlas dev.ultreon.quantum.client.management.TextureAtlasManager.register(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.atlas.TextureAtlas)"""
        return 'atlas.TextureAtlas'._wrap(super(_TextureAtlasManager, self).register(arg0, arg1))

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(_Manager, self).reload(arg0, arg1)

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
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.management.TextureAtlasManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(_TextureAtlasManager, self).reload(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.management.TextureAtlasManager 
 
 
# CLASS: dev.ultreon.quantum.client.management.ShaderProgramManager
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
from builtins import str
import dev.ultreon.quantum.client.management.Manager as _Manager
_Manager = _Manager
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.client.management.ShaderProgramManager as _ShaderProgramManager
_ShaderProgramManager = _ShaderProgramManager
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

from builtins import bool
import java.lang.Long as _long
import java.util.function.Supplier as _Supplier
_Supplier = _Supplier
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShaderProgramManager():
    """dev.ultreon.quantum.client.management.ShaderProgramManager"""
 
    @staticmethod
    def _wrap(java_value: _ShaderProgramManager) -> 'ShaderProgramManager':
        return ShaderProgramManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShaderProgramManager):
        """
        Dynamic initializer for ShaderProgramManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShaderProgramManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShaderProgramManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.management.ShaderProgramManager()"""
        val = _ShaderProgramManager()
        self.__wrapper = val

    @override
    @overload
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.management.ShaderProgramManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(_ShaderProgramManager, self).reload(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: 'Identifier') -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram dev.ultreon.quantum.client.management.ShaderProgramManager.get(dev.ultreon.quantum.util.Identifier)"""
        return 'glutils.ShaderProgram'._wrap(super(_ShaderProgramManager, self).get(arg0))

    @overload
    def register(self, arg0: 'Identifier', arg1: 'Supplier') -> 'Supplier':
        """public java.util.function.Supplier<com.badlogic.gdx.graphics.glutils.ShaderProgram> dev.ultreon.quantum.client.management.ShaderProgramManager.register(dev.ultreon.quantum.util.Identifier,java.util.function.Supplier<com.badlogic.gdx.graphics.glutils.ShaderProgram>)"""
        return 'Supplier'._wrap(super(_ShaderProgramManager, self).register(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(_Manager, self).reload(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.management.ShaderProgramManager()"""
        val = _ShaderProgramManager()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def register(self, arg0: 'Identifier', arg1: 'ShaderProgram') -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram dev.ultreon.quantum.client.management.ShaderProgramManager.register(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        return 'glutils.ShaderProgram'._wrap(super(_ShaderProgramManager, self).register(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.management.ShaderProviderManager
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
import dev.ultreon.quantum.client.management.Manager as _Manager
_Manager = _Manager
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.management.ShaderProviderManager as _ShaderProviderManager
_ShaderProviderManager = _ShaderProviderManager
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.utils.ShaderProvider as _ShaderProvider
_ShaderProvider = _ShaderProvider
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import com.google.common.base.Supplier as _Supplier
_Supplier = _Supplier
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShaderProviderManager():
    """dev.ultreon.quantum.client.management.ShaderProviderManager"""
 
    @staticmethod
    def _wrap(java_value: _ShaderProviderManager) -> 'ShaderProviderManager':
        return ShaderProviderManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShaderProviderManager):
        """
        Dynamic initializer for ShaderProviderManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShaderProviderManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShaderProviderManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.management.ShaderProviderManager()"""
        val = _ShaderProviderManager()
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
    def register(self, arg0: 'Identifier', arg1: 'Supplier') -> 'base.Supplier':
        """public <T extends com.badlogic.gdx.graphics.g3d.utils.ShaderProvider> com.google.common.base.Supplier<T> dev.ultreon.quantum.client.management.ShaderProviderManager.register(dev.ultreon.quantum.util.Identifier,com.google.common.base.Supplier<T>)"""
        return 'base.Supplier'._wrap(super(_ShaderProviderManager, self).register(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(_Manager, self).reload(arg0, arg1)

    @overload
    def register(self, arg0: 'Identifier', arg1: 'ShaderProvider') -> 'utils.ShaderProvider':
        """public com.badlogic.gdx.graphics.g3d.utils.ShaderProvider dev.ultreon.quantum.client.management.ShaderProviderManager.register(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g3d.utils.ShaderProvider)"""
        return 'utils.ShaderProvider'._wrap(super(_ShaderProviderManager, self).register(arg0, arg1))

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
    def get(self, arg0: 'Identifier') -> 'utils.ShaderProvider':
        """public com.badlogic.gdx.graphics.g3d.utils.ShaderProvider dev.ultreon.quantum.client.management.ShaderProviderManager.get(dev.ultreon.quantum.util.Identifier)"""
        return 'utils.ShaderProvider'._wrap(super(_ShaderProviderManager, self).get(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.management.ShaderProviderManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(_ShaderProviderManager, self).reload(arg0)

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.management.ShaderProviderManager()"""
        val = _ShaderProviderManager()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.management.Manager
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.client.management.Manager as _Manager
_Manager = _Manager
from pyquantum_helper import override
from abc import abstractmethod, ABC
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

 
class Manager():
    """dev.ultreon.quantum.client.management.Manager"""
 
    @staticmethod
    def _wrap(java_value: _Manager) -> 'Manager':
        return Manager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Manager):
        """
        Dynamic initializer for Manager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Manager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Manager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def register(self, arg0: 'Identifier', arg1: object):
        """public abstract T dev.ultreon.quantum.client.management.Manager.register(dev.ultreon.quantum.util.Identifier,T)"""
        pass

    @abstractmethod
    def reload(self, arg0: 'ReloadContext'):
        """public abstract void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        pass

    @abstractmethod
    def get(self, arg0: 'Identifier'):
        """public abstract T dev.ultreon.quantum.client.management.Manager.get(dev.ultreon.quantum.util.Identifier)"""
        pass

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(_Manager, self).reload(arg0, arg1) 
 
 
# CLASS: dev.ultreon.quantum.client.management.CubemapManager
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.client.management.Manager as _Manager
_Manager = _Manager
from pyquantum_helper import override
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

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.Cubemap as _Cubemap
_Cubemap = _Cubemap
import dev.ultreon.quantum.client.management.CubemapManager as _CubemapManager
_CubemapManager = _CubemapManager
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
 
class CubemapManager():
    """dev.ultreon.quantum.client.management.CubemapManager"""
 
    @staticmethod
    def _wrap(java_value: _CubemapManager) -> 'CubemapManager':
        return CubemapManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CubemapManager):
        """
        Dynamic initializer for CubemapManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CubemapManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CubemapManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.management.CubemapManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(_CubemapManager, self).reload(arg0)

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
    def register(self, arg0: 'Identifier', arg1: 'Cubemap') -> 'graphics.Cubemap':
        """public com.badlogic.gdx.graphics.Cubemap dev.ultreon.quantum.client.management.CubemapManager.register(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Cubemap)"""
        return 'graphics.Cubemap'._wrap(super(_CubemapManager, self).register(arg0, arg1))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.management.CubemapManager.dispose()"""
        super(CubemapManager, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(_Manager, self).reload(arg0, arg1)

    @overload
    def loadCubemap(self, arg0: 'Identifier'):
        """public void dev.ultreon.quantum.client.management.CubemapManager.loadCubemap(dev.ultreon.quantum.util.Identifier)"""
        super(_CubemapManager, self).loadCubemap(arg0)

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
    def __init__(self, arg0: 'ResourceManager'):
        """public dev.ultreon.quantum.client.management.CubemapManager(dev.ultreon.quantum.resources.ResourceManager)"""
        val = _CubemapManager(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: 'Identifier') -> 'graphics.Cubemap':
        """public com.badlogic.gdx.graphics.Cubemap dev.ultreon.quantum.client.management.CubemapManager.get(dev.ultreon.quantum.util.Identifier)"""
        return 'graphics.Cubemap'._wrap(super(_CubemapManager, self).get(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.client.management.MaterialManager
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.client.management.Manager as _Manager
_Manager = _Manager
from pyquantum_helper import override
try:
    from pyquantum.client import texture
except ImportError:
    texture = _import_once("pyquantum.client.texture")

import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.management.MaterialManager as _MaterialManager
_MaterialManager = _MaterialManager
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

import com.badlogic.gdx.graphics.g3d.Material as _Material
_Material = _Material
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MaterialManager():
    """dev.ultreon.quantum.client.management.MaterialManager"""
 
    @staticmethod
    def _wrap(java_value: _MaterialManager) -> 'MaterialManager':
        return MaterialManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MaterialManager):
        """
        Dynamic initializer for MaterialManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MaterialManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MaterialManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.management.MaterialManager.DEFAULT_ID
    DEFAULT_ID: 'util.Identifier' = _wrap(_util.Identifier.DEFAULT_ID)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def register(self, arg0: 'Identifier', arg1: 'Material') -> 'g3d.Material':
        """public com.badlogic.gdx.graphics.g3d.Material dev.ultreon.quantum.client.management.MaterialManager.register(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'g3d.Material'._wrap(super(_MaterialManager, self).register(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'ResourceManager', arg1: 'TextureManager', arg2: 'CubemapManager'):
        """public dev.ultreon.quantum.client.management.MaterialManager(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.client.texture.TextureManager,dev.ultreon.quantum.client.management.CubemapManager)"""
        val = _MaterialManager(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.management.MaterialManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(_MaterialManager, self).reload(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(_Manager, self).reload(arg0, arg1)

    @overload
    def get(self, arg0: 'Identifier') -> 'g3d.Material':
        """public com.badlogic.gdx.graphics.g3d.Material dev.ultreon.quantum.client.management.MaterialManager.get(dev.ultreon.quantum.util.Identifier)"""
        return 'g3d.Material'._wrap(super(_MaterialManager, self).get(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())