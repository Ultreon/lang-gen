from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client import atlas
except ImportError:
    atlas = __import_once__("pyquantum.client.atlas")

try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import dev.ultreon.quantum.client.management.Manager as __Manager
__Manager = __Manager
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import dev.ultreon.quantum.client.management.TextureAtlasManager as __TextureAtlasManager
__TextureAtlasManager = __TextureAtlasManager
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.atlas.TextureAtlas as __TextureAtlas
__TextureAtlas = __TextureAtlas
from builtins import int
 
class TextureAtlasManager():
    """dev.ultreon.quantum.client.management.TextureAtlasManager"""
 
    @staticmethod
    def __wrap(java_value: __TextureAtlasManager) -> 'TextureAtlasManager':
        return TextureAtlasManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureAtlasManager):
        """
        Dynamic initializer for TextureAtlasManager.
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
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.management.TextureAtlasManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(__TextureAtlasManager, self).reload(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def register(self, arg0: 'Identifier', arg1: 'TextureAtlas') -> 'atlas.TextureAtlas':
        """public dev.ultreon.quantum.client.atlas.TextureAtlas dev.ultreon.quantum.client.management.TextureAtlasManager.register(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.atlas.TextureAtlas)"""
        return 'atlas.TextureAtlas'.__wrap(super(__TextureAtlasManager, self).register(arg0, arg1))

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(__Manager, self).reload(arg0, arg1)

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.management.TextureAtlasManager(dev.ultreon.quantum.client.QuantumClient)"""
        val = __TextureAtlasManager(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: 'Identifier') -> 'atlas.TextureAtlas':
        """public dev.ultreon.quantum.client.atlas.TextureAtlas dev.ultreon.quantum.client.management.TextureAtlasManager.get(dev.ultreon.quantum.util.Identifier)"""
        return 'atlas.TextureAtlas'.__wrap(super(__TextureAtlasManager, self).get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.management.TextureAtlasManager
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client import atlas
except ImportError:
    atlas = __import_once__("pyquantum.client.atlas")

try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import dev.ultreon.quantum.client.management.Manager as __Manager
__Manager = __Manager
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import dev.ultreon.quantum.client.management.TextureAtlasManager as __TextureAtlasManager
__TextureAtlasManager = __TextureAtlasManager
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.atlas.TextureAtlas as __TextureAtlas
__TextureAtlas = __TextureAtlas
from builtins import int
 
class TextureAtlasManager():
    """dev.ultreon.quantum.client.management.TextureAtlasManager"""
 
    @staticmethod
    def __wrap(java_value: __TextureAtlasManager) -> 'TextureAtlasManager':
        return TextureAtlasManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureAtlasManager):
        """
        Dynamic initializer for TextureAtlasManager.
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
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.management.TextureAtlasManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(__TextureAtlasManager, self).reload(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def register(self, arg0: 'Identifier', arg1: 'TextureAtlas') -> 'atlas.TextureAtlas':
        """public dev.ultreon.quantum.client.atlas.TextureAtlas dev.ultreon.quantum.client.management.TextureAtlasManager.register(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.atlas.TextureAtlas)"""
        return 'atlas.TextureAtlas'.__wrap(super(__TextureAtlasManager, self).register(arg0, arg1))

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(__Manager, self).reload(arg0, arg1)

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.management.TextureAtlasManager(dev.ultreon.quantum.client.QuantumClient)"""
        val = __TextureAtlasManager(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: 'Identifier') -> 'atlas.TextureAtlas':
        """public dev.ultreon.quantum.client.atlas.TextureAtlas dev.ultreon.quantum.client.management.TextureAtlasManager.get(dev.ultreon.quantum.util.Identifier)"""
        return 'atlas.TextureAtlas'.__wrap(super(__TextureAtlasManager, self).get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.management.TextureAtlasManager 
 
 
# CLASS: dev.ultreon.quantum.client.management.ShaderProgramManager
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.glutils.ShaderProgram as __ShaderProgram
__ShaderProgram = __ShaderProgram
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.management.Manager as __Manager
__Manager = __Manager
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.client.management.ShaderProgramManager as __ShaderProgramManager
__ShaderProgramManager = __ShaderProgramManager
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.util.function.Supplier as __Supplier
__Supplier = __Supplier
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ShaderProgramManager():
    """dev.ultreon.quantum.client.management.ShaderProgramManager"""
 
    @staticmethod
    def __wrap(java_value: __ShaderProgramManager) -> 'ShaderProgramManager':
        return ShaderProgramManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShaderProgramManager):
        """
        Dynamic initializer for ShaderProgramManager.
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
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.management.ShaderProgramManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(__ShaderProgramManager, self).reload(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.management.ShaderProgramManager()"""
        val = __ShaderProgramManager()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def register(self, arg0: 'Identifier', arg1: 'Supplier') -> 'Supplier':
        """public java.util.function.Supplier<com.badlogic.gdx.graphics.glutils.ShaderProgram> dev.ultreon.quantum.client.management.ShaderProgramManager.register(dev.ultreon.quantum.util.Identifier,java.util.function.Supplier<com.badlogic.gdx.graphics.glutils.ShaderProgram>)"""
        return 'Supplier'.__wrap(super(__ShaderProgramManager, self).register(arg0, arg1))

    @overload
    def register(self, arg0: 'Identifier', arg1: 'ShaderProgram') -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram dev.ultreon.quantum.client.management.ShaderProgramManager.register(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        return 'glutils.ShaderProgram'.__wrap(super(__ShaderProgramManager, self).register(arg0, arg1))

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(__Manager, self).reload(arg0, arg1)

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def get(self, arg0: 'Identifier') -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram dev.ultreon.quantum.client.management.ShaderProgramManager.get(dev.ultreon.quantum.util.Identifier)"""
        return 'glutils.ShaderProgram'.__wrap(super(__ShaderProgramManager, self).get(arg0))

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.management.ShaderProgramManager()"""
        val = __ShaderProgramManager()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.management.ShaderProviderManager
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.management.Manager as __Manager
__Manager = __Manager
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.management.ShaderProviderManager as __ShaderProviderManager
__ShaderProviderManager = __ShaderProviderManager
import java.lang.Object as __Object
__Object = __Object
import com.google.common.base.Supplier as __Supplier
__Supplier = __Supplier
import com.badlogic.gdx.graphics.g3d.utils.ShaderProvider as __ShaderProvider
__ShaderProvider = __ShaderProvider
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class ShaderProviderManager():
    """dev.ultreon.quantum.client.management.ShaderProviderManager"""
 
    @staticmethod
    def __wrap(java_value: __ShaderProviderManager) -> 'ShaderProviderManager':
        return ShaderProviderManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShaderProviderManager):
        """
        Dynamic initializer for ShaderProviderManager.
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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.management.ShaderProviderManager()"""
        val = __ShaderProviderManager()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.management.ShaderProviderManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(__ShaderProviderManager, self).reload(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.management.ShaderProviderManager()"""
        val = __ShaderProviderManager()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def register(self, arg0: 'Identifier', arg1: 'Supplier') -> 'base.Supplier':
        """public <T extends com.badlogic.gdx.graphics.g3d.utils.ShaderProvider> com.google.common.base.Supplier<T> dev.ultreon.quantum.client.management.ShaderProviderManager.register(dev.ultreon.quantum.util.Identifier,com.google.common.base.Supplier<T>)"""
        return 'base.Supplier'.__wrap(super(__ShaderProviderManager, self).register(arg0, arg1))

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(__Manager, self).reload(arg0, arg1)

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def register(self, arg0: 'Identifier', arg1: 'ShaderProvider') -> 'utils.ShaderProvider':
        """public com.badlogic.gdx.graphics.g3d.utils.ShaderProvider dev.ultreon.quantum.client.management.ShaderProviderManager.register(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g3d.utils.ShaderProvider)"""
        return 'utils.ShaderProvider'.__wrap(super(__ShaderProviderManager, self).register(arg0, arg1))

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
    def get(self, arg0: 'Identifier') -> 'utils.ShaderProvider':
        """public com.badlogic.gdx.graphics.g3d.utils.ShaderProvider dev.ultreon.quantum.client.management.ShaderProviderManager.get(dev.ultreon.quantum.util.Identifier)"""
        return 'utils.ShaderProvider'.__wrap(super(__ShaderProviderManager, self).get(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.management.Manager
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

from pyquantum_helper import override
import dev.ultreon.quantum.client.management.Manager as __Manager
__Manager = __Manager
from abc import abstractmethod, ABC
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

 
class Manager(ABC):
    """dev.ultreon.quantum.client.management.Manager"""
 
    @staticmethod
    def __wrap(java_value: __Manager) -> 'Manager':
        return Manager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Manager):
        """
        Dynamic initializer for Manager.
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
    def register(self, arg0: 'Identifier', arg1: object):
        """public abstract T dev.ultreon.quantum.client.management.Manager.register(dev.ultreon.quantum.util.Identifier,T)"""
        pass

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(__Manager, self).reload(arg0, arg1)

    @abstractmethod
    def reload(self, arg0: 'ReloadContext'):
        """public abstract void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        pass

    @abstractmethod
    def get(self, arg0: 'Identifier'):
        """public abstract T dev.ultreon.quantum.client.management.Manager.get(dev.ultreon.quantum.util.Identifier)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.management.CubemapManager
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.Cubemap as __Cubemap
__Cubemap = __Cubemap
import dev.ultreon.quantum.client.management.Manager as __Manager
__Manager = __Manager
import dev.ultreon.quantum.client.management.CubemapManager as __CubemapManager
__CubemapManager = __CubemapManager
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
 
class CubemapManager():
    """dev.ultreon.quantum.client.management.CubemapManager"""
 
    @staticmethod
    def __wrap(java_value: __CubemapManager) -> 'CubemapManager':
        return CubemapManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CubemapManager):
        """
        Dynamic initializer for CubemapManager.
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
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.management.CubemapManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(__CubemapManager, self).reload(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(__Manager, self).reload(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.management.CubemapManager.dispose()"""
        super(CubemapManager, self).dispose()

    @overload
    def loadCubemap(self, arg0: 'Identifier'):
        """public void dev.ultreon.quantum.client.management.CubemapManager.loadCubemap(dev.ultreon.quantum.util.Identifier)"""
        super(__CubemapManager, self).loadCubemap(arg0)

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
    def get(self, arg0: 'Identifier') -> 'graphics.Cubemap':
        """public com.badlogic.gdx.graphics.Cubemap dev.ultreon.quantum.client.management.CubemapManager.get(dev.ultreon.quantum.util.Identifier)"""
        return 'graphics.Cubemap'.__wrap(super(__CubemapManager, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'ResourceManager'):
        """public dev.ultreon.quantum.client.management.CubemapManager(dev.ultreon.quantum.resources.ResourceManager)"""
        val = __CubemapManager(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def register(self, arg0: 'Identifier', arg1: 'Cubemap') -> 'graphics.Cubemap':
        """public com.badlogic.gdx.graphics.Cubemap dev.ultreon.quantum.client.management.CubemapManager.register(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Cubemap)"""
        return 'graphics.Cubemap'.__wrap(super(__CubemapManager, self).register(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.management.MaterialManager
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.client import texture
except ImportError:
    texture = __import_once__("pyquantum.client.texture")

import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import dev.ultreon.quantum.client.management.Manager as __Manager
__Manager = __Manager
import dev.ultreon.quantum.client.management.MaterialManager as __MaterialManager
__MaterialManager = __MaterialManager
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
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.Material as __Material
__Material = __Material
from builtins import bool
from builtins import int
 
class MaterialManager():
    """dev.ultreon.quantum.client.management.MaterialManager"""
 
    @staticmethod
    def __wrap(java_value: __MaterialManager) -> 'MaterialManager':
        return MaterialManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MaterialManager):
        """
        Dynamic initializer for MaterialManager.
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
 
    # public static final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.management.MaterialManager.DEFAULT_ID
    DEFAULT_ID: 'util.Identifier' = __wrap(__util.Identifier.DEFAULT_ID)


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
    def register(self, arg0: 'Identifier', arg1: 'Material') -> 'g3d.Material':
        """public com.badlogic.gdx.graphics.g3d.Material dev.ultreon.quantum.client.management.MaterialManager.register(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.g3d.Material)"""
        return 'g3d.Material'.__wrap(super(__MaterialManager, self).register(arg0, arg1))

    @override
    @overload
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public default void dev.ultreon.quantum.client.management.Manager.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        super(__Manager, self).reload(arg0, arg1)

    @override
    @overload
    def reload(self, arg0: 'ReloadContext'):
        """public void dev.ultreon.quantum.client.management.MaterialManager.reload(dev.ultreon.quantum.resources.ReloadContext)"""
        super(__MaterialManager, self).reload(arg0)

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
    def __init__(self, arg0: 'ResourceManager', arg1: 'TextureManager', arg2: 'CubemapManager'):
        """public dev.ultreon.quantum.client.management.MaterialManager(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.client.texture.TextureManager,dev.ultreon.quantum.client.management.CubemapManager)"""
        val = __MaterialManager(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def get(self, arg0: 'Identifier') -> 'g3d.Material':
        """public com.badlogic.gdx.graphics.g3d.Material dev.ultreon.quantum.client.management.MaterialManager.get(dev.ultreon.quantum.util.Identifier)"""
        return 'g3d.Material'.__wrap(super(__MaterialManager, self).get(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))