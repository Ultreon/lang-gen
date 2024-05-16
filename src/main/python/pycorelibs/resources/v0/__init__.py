from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.io.File as File
import java.nio.file.Path as Path
import dev.ultreon.libs.resources.v0.ResourceManager as _ResourceManager
_ResourceManager = _ResourceManager
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.net.URL as URL
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

import dev.ultreon.libs.resources.v0.Resource as _Resource
_Resource = _Resource
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ResourceManager():
    """dev.ultreon.libs.resources.v0.ResourceManager"""
 
    @staticmethod
    def _wrap(java_value: _ResourceManager) -> 'ResourceManager':
        return ResourceManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ResourceManager):
        """
        Dynamic initializer for ResourceManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ResourceManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ResourceManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.libs.resources.v0.ResourceManager(java.lang.String)"""
        val = _ResourceManager(arg0)
        self.__wrapper = val

    @overload
    def getResource(self, arg0: 'Identifier') -> 'Resource':
        """public dev.ultreon.libs.resources.v0.Resource dev.ultreon.libs.resources.v0.ResourceManager.getResource(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'Resource'._wrap(super(_ResourceManager, self).getResource(arg0))

    @overload
    def importPackage(self, arg0: 'File'):
        """public void dev.ultreon.libs.resources.v0.ResourceManager.importPackage(java.io.File) throws java.io.IOException"""
        super(_ResourceManager, self).importPackage(arg0)

    @overload
    def importDeferredPackage(self, arg0: 'Class'):
        """public void dev.ultreon.libs.resources.v0.ResourceManager.importDeferredPackage(java.lang.Class<?>)"""
        super(_ResourceManager, self).importDeferredPackage(arg0)

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
    def openResourceStream(self, arg0: 'Identifier') -> 'InputStream':
        """public java.io.InputStream dev.ultreon.libs.resources.v0.ResourceManager.openResourceStream(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'InputStream'._wrap(super(_ResourceManager, self).openResourceStream(arg0))

    @overload
    def getAllDataById(self, arg0: 'Identifier') -> 'List':
        """public java.util.List<byte[]> dev.ultreon.libs.resources.v0.ResourceManager.getAllDataById(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'List'._wrap(super(_ResourceManager, self).getAllDataById(arg0))

    @overload
    def importPackage(self, arg0: 'URL'):
        """public void dev.ultreon.libs.resources.v0.ResourceManager.importPackage(java.net.URL) throws java.io.IOException"""
        super(_ResourceManager, self).importPackage(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def importPackage(self, arg0: 'Path'):
        """public void dev.ultreon.libs.resources.v0.ResourceManager.importPackage(java.nio.file.Path) throws java.io.IOException"""
        super(_ResourceManager, self).importPackage(arg0)

    @overload
    def getRoot(self) -> str:
        """public java.lang.String dev.ultreon.libs.resources.v0.ResourceManager.getRoot()"""
        return str._wrap(super(ResourceManager, self).getRoot())

    @overload
    def getAllDataByPath(self, arg0: str) -> 'List':
        """public java.util.List<byte[]> dev.ultreon.libs.resources.v0.ResourceManager.getAllDataByPath(java.lang.String)"""
        return 'List'._wrap(super(_ResourceManager, self).getAllDataByPath(arg0))

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
    def canScanFiles(self) -> bool:
        """public boolean dev.ultreon.libs.resources.v0.ResourceManager.canScanFiles()"""
        return bool._wrap(super(ResourceManager, self).canScanFiles())

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

 
 
 
# CLASS: dev.ultreon.libs.resources.v0.ResourceManager
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.io.File as File
import java.nio.file.Path as Path
import dev.ultreon.libs.resources.v0.ResourceManager as _ResourceManager
_ResourceManager = _ResourceManager
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.net.URL as URL
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

import dev.ultreon.libs.resources.v0.Resource as _Resource
_Resource = _Resource
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ResourceManager():
    """dev.ultreon.libs.resources.v0.ResourceManager"""
 
    @staticmethod
    def _wrap(java_value: _ResourceManager) -> 'ResourceManager':
        return ResourceManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ResourceManager):
        """
        Dynamic initializer for ResourceManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ResourceManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ResourceManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.libs.resources.v0.ResourceManager(java.lang.String)"""
        val = _ResourceManager(arg0)
        self.__wrapper = val

    @overload
    def getResource(self, arg0: 'Identifier') -> 'Resource':
        """public dev.ultreon.libs.resources.v0.Resource dev.ultreon.libs.resources.v0.ResourceManager.getResource(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'Resource'._wrap(super(_ResourceManager, self).getResource(arg0))

    @overload
    def importPackage(self, arg0: 'File'):
        """public void dev.ultreon.libs.resources.v0.ResourceManager.importPackage(java.io.File) throws java.io.IOException"""
        super(_ResourceManager, self).importPackage(arg0)

    @overload
    def importDeferredPackage(self, arg0: 'Class'):
        """public void dev.ultreon.libs.resources.v0.ResourceManager.importDeferredPackage(java.lang.Class<?>)"""
        super(_ResourceManager, self).importDeferredPackage(arg0)

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
    def openResourceStream(self, arg0: 'Identifier') -> 'InputStream':
        """public java.io.InputStream dev.ultreon.libs.resources.v0.ResourceManager.openResourceStream(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'InputStream'._wrap(super(_ResourceManager, self).openResourceStream(arg0))

    @overload
    def getAllDataById(self, arg0: 'Identifier') -> 'List':
        """public java.util.List<byte[]> dev.ultreon.libs.resources.v0.ResourceManager.getAllDataById(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'List'._wrap(super(_ResourceManager, self).getAllDataById(arg0))

    @overload
    def importPackage(self, arg0: 'URL'):
        """public void dev.ultreon.libs.resources.v0.ResourceManager.importPackage(java.net.URL) throws java.io.IOException"""
        super(_ResourceManager, self).importPackage(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def importPackage(self, arg0: 'Path'):
        """public void dev.ultreon.libs.resources.v0.ResourceManager.importPackage(java.nio.file.Path) throws java.io.IOException"""
        super(_ResourceManager, self).importPackage(arg0)

    @overload
    def getRoot(self) -> str:
        """public java.lang.String dev.ultreon.libs.resources.v0.ResourceManager.getRoot()"""
        return str._wrap(super(ResourceManager, self).getRoot())

    @overload
    def getAllDataByPath(self, arg0: str) -> 'List':
        """public java.util.List<byte[]> dev.ultreon.libs.resources.v0.ResourceManager.getAllDataByPath(java.lang.String)"""
        return 'List'._wrap(super(_ResourceManager, self).getAllDataByPath(arg0))

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
    def canScanFiles(self) -> bool:
        """public boolean dev.ultreon.libs.resources.v0.ResourceManager.canScanFiles()"""
        return bool._wrap(super(ResourceManager, self).canScanFiles())

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

 
 
 
# CLASS: dev.ultreon.libs.resources.v0.ResourceManager 
 
 
# CLASS: dev.ultreon.libs.resources.v0.ResourcePackage
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
import java.util.Set as Set
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

import dev.ultreon.libs.resources.v0.Resource as _Resource
_Resource = _Resource
import dev.ultreon.libs.resources.v0.ResourcePackage as _ResourcePackage
_ResourcePackage = _ResourcePackage
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ResourcePackage():
    """dev.ultreon.libs.resources.v0.ResourcePackage"""
 
    @staticmethod
    def _wrap(java_value: _ResourcePackage) -> 'ResourcePackage':
        return ResourcePackage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ResourcePackage):
        """
        Dynamic initializer for ResourcePackage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ResourcePackage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ResourcePackage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.libs.commons.v0.Identifier, dev.ultreon.libs.resources.v0.Resource> dev.ultreon.libs.resources.v0.ResourcePackage.mapEntries()"""
        return 'Map'._wrap(super(ResourcePackage, self).mapEntries())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.resources.v0.ResourcePackage()"""
        val = _ResourcePackage()
        self.__wrapper = val

    @overload
    def get(self, arg0: 'Identifier') -> 'Resource':
        """public dev.ultreon.libs.resources.v0.Resource dev.ultreon.libs.resources.v0.ResourcePackage.get(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'Resource'._wrap(super(_ResourcePackage, self).get(arg0))

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
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.libs.resources.v0.ResourcePackage.has(dev.ultreon.libs.commons.v0.Identifier)"""
        return bool._wrap(super(_ResourcePackage, self).has(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.commons.v0.Identifier> dev.ultreon.libs.resources.v0.ResourcePackage.entries()"""
        return 'Set'._wrap(super(ResourcePackage, self).entries())

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
    def __init__(self, arg0: 'Map'):
        """public dev.ultreon.libs.resources.v0.ResourcePackage(java.util.Map<dev.ultreon.libs.commons.v0.Identifier, dev.ultreon.libs.resources.v0.Resource>)"""
        val = _ResourcePackage(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.resources.v0.ResourcePackage()"""
        val = _ResourcePackage()
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
 
 
# CLASS: dev.ultreon.libs.resources.v0.Resource
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.io.ByteArrayInputStream as _ByteArrayInputStream
_ByteArrayInputStream = _ByteArrayInputStream
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.awt.Font as Font
import java.awt.image.BufferedImage as _BufferedImage
_BufferedImage = _BufferedImage
try:
    from pycorelibs.functions.v0 import misc
except ImportError:
    misc = _import_once("pycorelibs.functions.v0.misc")

import java.lang.String as _String
_String = _String
from typing import List
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.io.ByteArrayInputStream as ByteArrayInputStream
import java.lang.Integer as _int
import dev.ultreon.libs.resources.v0.Resource as _Resource
_Resource = _Resource
import java.io.InputStream as InputStream
import java.awt.image.BufferedImage as BufferedImage
import java.awt.Font as _Font
_Font = _Font
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Resource():
    """dev.ultreon.libs.resources.v0.Resource"""
 
    @staticmethod
    def _wrap(java_value: _Resource) -> 'Resource':
        return Resource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Resource):
        """
        Dynamic initializer for Resource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Resource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Resource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def load(self):
        """public void dev.ultreon.libs.resources.v0.Resource.load()"""
        super(Resource, self).load()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def readImage(self) -> 'BufferedImage':
        """public java.awt.image.BufferedImage dev.ultreon.libs.resources.v0.Resource.readImage() throws java.io.IOException"""
        return 'BufferedImage'._wrap(super(Resource, self).readImage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'ThrowingSupplier'):
        """public dev.ultreon.libs.resources.v0.Resource(dev.ultreon.libs.functions.v0.misc.ThrowingSupplier<java.io.InputStream, java.io.IOException>)"""
        val = _Resource(arg0)
        self.__wrapper = val

    @overload
    def getData(self) -> List[int]:
        """public byte[] dev.ultreon.libs.resources.v0.Resource.getData()"""
        return List[int]._wrap(super(Resource, self).getData())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def openStream(self) -> 'ByteArrayInputStream':
        """public java.io.ByteArrayInputStream dev.ultreon.libs.resources.v0.Resource.openStream()"""
        return 'ByteArrayInputStream'._wrap(super(Resource, self).openStream())

    @overload
    def loadOrOpenStream(self) -> 'InputStream':
        """public java.io.InputStream dev.ultreon.libs.resources.v0.Resource.loadOrOpenStream()"""
        return 'InputStream'._wrap(super(Resource, self).loadOrOpenStream())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def loadFont(self) -> 'Font':
        """public java.awt.Font dev.ultreon.libs.resources.v0.Resource.loadFont() throws java.awt.FontFormatException"""
        return 'Font'._wrap(super(Resource, self).loadFont())

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
    def loadOrGet(self) -> List[int]:
        """public byte[] dev.ultreon.libs.resources.v0.Resource.loadOrGet()"""
        return List[int]._wrap(super(Resource, self).loadOrGet())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())