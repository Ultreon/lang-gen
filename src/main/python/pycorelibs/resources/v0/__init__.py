from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.resources.v0.Resource as __Resource
__Resource = __Resource
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.awt.Font as Font
try:
    from pycorelibs.functions.v0 import misc
except ImportError:
    misc = __import_once__("pycorelibs.functions.v0.misc")

import java.io.InputStream as __InputStream
__InputStream = __InputStream
import java.awt.image.BufferedImage as __BufferedImage
__BufferedImage = __BufferedImage
from typing import List
import java.io.ByteArrayInputStream as __ByteArrayInputStream
__ByteArrayInputStream = __ByteArrayInputStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.ByteArrayInputStream as ByteArrayInputStream
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.awt.Font as __Font
__Font = __Font
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Resource():
    """dev.ultreon.libs.resources.v0.Resource"""
 
    @staticmethod
    def __wrap(java_value: __Resource) -> 'Resource':
        return Resource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Resource):
        """
        Dynamic initializer for Resource.
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
    def openStream(self) -> 'ByteArrayInputStream':
        """public java.io.ByteArrayInputStream dev.ultreon.libs.resources.v0.Resource.openStream()"""
        return 'ByteArrayInputStream'.__wrap(super(Resource, self).openStream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def load(self):
        """public void dev.ultreon.libs.resources.v0.Resource.load()"""
        super(Resource, self).load()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getData(self) -> List[int]:
        """public byte[] dev.ultreon.libs.resources.v0.Resource.getData()"""
        return List[int].__wrap(super(Resource, self).getData())

    @overload
    def readImage(self) -> 'BufferedImage':
        """public java.awt.image.BufferedImage dev.ultreon.libs.resources.v0.Resource.readImage() throws java.io.IOException"""
        return 'BufferedImage'.__wrap(super(Resource, self).readImage())

    @overload
    def loadFont(self) -> 'Font':
        """public java.awt.Font dev.ultreon.libs.resources.v0.Resource.loadFont() throws java.awt.FontFormatException"""
        return 'Font'.__wrap(super(Resource, self).loadFont())

    @overload
    def __init__(self, arg0: 'ThrowingSupplier'):
        """public dev.ultreon.libs.resources.v0.Resource(dev.ultreon.libs.functions.v0.misc.ThrowingSupplier<java.io.InputStream, java.io.IOException>)"""
        val = __Resource(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def loadOrGet(self) -> List[int]:
        """public byte[] dev.ultreon.libs.resources.v0.Resource.loadOrGet()"""
        return List[int].__wrap(super(Resource, self).loadOrGet())

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
    def loadOrOpenStream(self) -> 'InputStream':
        """public java.io.InputStream dev.ultreon.libs.resources.v0.Resource.loadOrOpenStream()"""
        return 'InputStream'.__wrap(super(Resource, self).loadOrOpenStream())

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

 
 
 
# CLASS: dev.ultreon.libs.resources.v0.Resource
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.resources.v0.Resource as __Resource
__Resource = __Resource
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.awt.Font as Font
try:
    from pycorelibs.functions.v0 import misc
except ImportError:
    misc = __import_once__("pycorelibs.functions.v0.misc")

import java.io.InputStream as __InputStream
__InputStream = __InputStream
import java.awt.image.BufferedImage as __BufferedImage
__BufferedImage = __BufferedImage
from typing import List
import java.io.ByteArrayInputStream as __ByteArrayInputStream
__ByteArrayInputStream = __ByteArrayInputStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.ByteArrayInputStream as ByteArrayInputStream
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.awt.Font as __Font
__Font = __Font
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Resource():
    """dev.ultreon.libs.resources.v0.Resource"""
 
    @staticmethod
    def __wrap(java_value: __Resource) -> 'Resource':
        return Resource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Resource):
        """
        Dynamic initializer for Resource.
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
    def openStream(self) -> 'ByteArrayInputStream':
        """public java.io.ByteArrayInputStream dev.ultreon.libs.resources.v0.Resource.openStream()"""
        return 'ByteArrayInputStream'.__wrap(super(Resource, self).openStream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def load(self):
        """public void dev.ultreon.libs.resources.v0.Resource.load()"""
        super(Resource, self).load()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getData(self) -> List[int]:
        """public byte[] dev.ultreon.libs.resources.v0.Resource.getData()"""
        return List[int].__wrap(super(Resource, self).getData())

    @overload
    def readImage(self) -> 'BufferedImage':
        """public java.awt.image.BufferedImage dev.ultreon.libs.resources.v0.Resource.readImage() throws java.io.IOException"""
        return 'BufferedImage'.__wrap(super(Resource, self).readImage())

    @overload
    def loadFont(self) -> 'Font':
        """public java.awt.Font dev.ultreon.libs.resources.v0.Resource.loadFont() throws java.awt.FontFormatException"""
        return 'Font'.__wrap(super(Resource, self).loadFont())

    @overload
    def __init__(self, arg0: 'ThrowingSupplier'):
        """public dev.ultreon.libs.resources.v0.Resource(dev.ultreon.libs.functions.v0.misc.ThrowingSupplier<java.io.InputStream, java.io.IOException>)"""
        val = __Resource(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def loadOrGet(self) -> List[int]:
        """public byte[] dev.ultreon.libs.resources.v0.Resource.loadOrGet()"""
        return List[int].__wrap(super(Resource, self).loadOrGet())

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
    def loadOrOpenStream(self) -> 'InputStream':
        """public java.io.InputStream dev.ultreon.libs.resources.v0.Resource.loadOrOpenStream()"""
        return 'InputStream'.__wrap(super(Resource, self).loadOrOpenStream())

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

 
 
 
# CLASS: dev.ultreon.libs.resources.v0.Resource 
 
 
# CLASS: dev.ultreon.libs.resources.v0.ResourceManager
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.resources.v0.Resource as __Resource
__Resource = __Resource
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import java.nio.file.Path as Path
import dev.ultreon.libs.resources.v0.ResourceManager as __ResourceManager
__ResourceManager = __ResourceManager
import java.io.InputStream as __InputStream
__InputStream = __InputStream
import java.net.URL as URL
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class ResourceManager():
    """dev.ultreon.libs.resources.v0.ResourceManager"""
 
    @staticmethod
    def __wrap(java_value: __ResourceManager) -> 'ResourceManager':
        return ResourceManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResourceManager):
        """
        Dynamic initializer for ResourceManager.
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
    def getAllDataByPath(self, arg0: str) -> 'List':
        """public java.util.List<byte[]> dev.ultreon.libs.resources.v0.ResourceManager.getAllDataByPath(java.lang.String)"""
        return 'List'.__wrap(super(__ResourceManager, self).getAllDataByPath(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def canScanFiles(self) -> bool:
        """public boolean dev.ultreon.libs.resources.v0.ResourceManager.canScanFiles()"""
        return bool.__wrap(super(ResourceManager, self).canScanFiles())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAllDataById(self, arg0: 'Identifier') -> 'List':
        """public java.util.List<byte[]> dev.ultreon.libs.resources.v0.ResourceManager.getAllDataById(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'List'.__wrap(super(__ResourceManager, self).getAllDataById(arg0))

    @overload
    def importPackage(self, arg0: 'Path'):
        """public void dev.ultreon.libs.resources.v0.ResourceManager.importPackage(java.nio.file.Path) throws java.io.IOException"""
        super(__ResourceManager, self).importPackage(arg0)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.libs.resources.v0.ResourceManager(java.lang.String)"""
        val = __ResourceManager(arg0)
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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getRoot(self) -> str:
        """public java.lang.String dev.ultreon.libs.resources.v0.ResourceManager.getRoot()"""
        return str.__wrap(super(ResourceManager, self).getRoot())

    @overload
    def importPackage(self, arg0: 'URL'):
        """public void dev.ultreon.libs.resources.v0.ResourceManager.importPackage(java.net.URL) throws java.io.IOException"""
        super(__ResourceManager, self).importPackage(arg0)

    @overload
    def openResourceStream(self, arg0: 'Identifier') -> 'InputStream':
        """public java.io.InputStream dev.ultreon.libs.resources.v0.ResourceManager.openResourceStream(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'InputStream'.__wrap(super(__ResourceManager, self).openResourceStream(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getResource(self, arg0: 'Identifier') -> 'Resource':
        """public dev.ultreon.libs.resources.v0.Resource dev.ultreon.libs.resources.v0.ResourceManager.getResource(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'Resource'.__wrap(super(__ResourceManager, self).getResource(arg0))

    @overload
    def importPackage(self, arg0: 'File'):
        """public void dev.ultreon.libs.resources.v0.ResourceManager.importPackage(java.io.File) throws java.io.IOException"""
        super(__ResourceManager, self).importPackage(arg0)

    @overload
    def importDeferredPackage(self, arg0: 'Class'):
        """public void dev.ultreon.libs.resources.v0.ResourceManager.importDeferredPackage(java.lang.Class<?>)"""
        super(__ResourceManager, self).importDeferredPackage(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.libs.resources.v0.ResourcePackage
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.libs.resources.v0.Resource as __Resource
__Resource = __Resource
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.String as __String
__String = __String
import dev.ultreon.libs.resources.v0.ResourcePackage as __ResourcePackage
__ResourcePackage = __ResourcePackage
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class ResourcePackage():
    """dev.ultreon.libs.resources.v0.ResourcePackage"""
 
    @staticmethod
    def __wrap(java_value: __ResourcePackage) -> 'ResourcePackage':
        return ResourcePackage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResourcePackage):
        """
        Dynamic initializer for ResourcePackage.
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
        """public dev.ultreon.libs.resources.v0.ResourcePackage()"""
        val = __ResourcePackage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.commons.v0.Identifier> dev.ultreon.libs.resources.v0.ResourcePackage.entries()"""
        return 'Set'.__wrap(super(ResourcePackage, self).entries())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.resources.v0.ResourcePackage()"""
        val = __ResourcePackage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.libs.resources.v0.ResourcePackage.has(dev.ultreon.libs.commons.v0.Identifier)"""
        return bool.__wrap(super(__ResourcePackage, self).has(arg0))

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
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.libs.commons.v0.Identifier, dev.ultreon.libs.resources.v0.Resource> dev.ultreon.libs.resources.v0.ResourcePackage.mapEntries()"""
        return 'Map'.__wrap(super(ResourcePackage, self).mapEntries())

    @overload
    def __init__(self, arg0: 'Map'):
        """public dev.ultreon.libs.resources.v0.ResourcePackage(java.util.Map<dev.ultreon.libs.commons.v0.Identifier, dev.ultreon.libs.resources.v0.Resource>)"""
        val = __ResourcePackage(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def get(self, arg0: 'Identifier') -> 'Resource':
        """public dev.ultreon.libs.resources.v0.Resource dev.ultreon.libs.resources.v0.ResourcePackage.get(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'Resource'.__wrap(super(__ResourcePackage, self).get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))