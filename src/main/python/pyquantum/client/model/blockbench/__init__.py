from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace as __BBModelMeshFace
__BBModelMeshFace = __BBModelMeshFace
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
import java.util.List as List
 
class BBModelMeshFace():
    """dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace"""
 
    @staticmethod
    def __wrap(java_value: __BBModelMeshFace) -> 'BBModelMeshFace':
        return BBModelMeshFace(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBModelMeshFace):
        """
        Dynamic initializer for BBModelMeshFace.
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
 
    @overload
    def uvs(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.libs.commons.v0.vector.Vec2f> dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.uvs()"""
        return 'Map'.__wrap(super(BBModelMeshFace, self).uvs())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.hashCode()"""
        return int.__wrap(super(BBModelMeshFace, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.toString()"""
        return str.__wrap(super(BBModelMeshFace, self).toString())

    @overload
    def texture(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.texture()"""
        return int.__wrap(super(BBModelMeshFace, self).texture())

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
    def vertices(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelVertex> dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.vertices()"""
        return 'List'.__wrap(super(BBModelMeshFace, self).vertices())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Map', arg1: 'List', arg2: int):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace(java.util.Map<java.lang.String, dev.ultreon.libs.commons.v0.vector.Vec2f>,java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelVertex>,int)"""
        val = __BBModelMeshFace(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBModelMeshFace, self).equals(arg0))

    @overload
    def write(self, arg0: 'ModelBuilder', arg1: 'Map', arg2: 'Map', arg3: 'Vec2f'):
        """public void dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.write(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.lang.Integer, dev.ultreon.quantum.client.model.blockbench.BBTexture>,java.util.Map<dev.ultreon.quantum.client.model.blockbench.BBTexture, com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder>,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__BBModelMeshFace, self).write(arg0, arg1, arg2, arg3)

 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace as __BBModelMeshFace
__BBModelMeshFace = __BBModelMeshFace
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
import java.util.List as List
 
class BBModelMeshFace():
    """dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace"""
 
    @staticmethod
    def __wrap(java_value: __BBModelMeshFace) -> 'BBModelMeshFace':
        return BBModelMeshFace(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBModelMeshFace):
        """
        Dynamic initializer for BBModelMeshFace.
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
 
    @overload
    def uvs(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.libs.commons.v0.vector.Vec2f> dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.uvs()"""
        return 'Map'.__wrap(super(BBModelMeshFace, self).uvs())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.hashCode()"""
        return int.__wrap(super(BBModelMeshFace, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.toString()"""
        return str.__wrap(super(BBModelMeshFace, self).toString())

    @overload
    def texture(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.texture()"""
        return int.__wrap(super(BBModelMeshFace, self).texture())

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
    def vertices(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelVertex> dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.vertices()"""
        return 'List'.__wrap(super(BBModelMeshFace, self).vertices())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Map', arg1: 'List', arg2: int):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace(java.util.Map<java.lang.String, dev.ultreon.libs.commons.v0.vector.Vec2f>,java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelVertex>,int)"""
        val = __BBModelMeshFace(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBModelMeshFace, self).equals(arg0))

    @overload
    def write(self, arg0: 'ModelBuilder', arg1: 'Map', arg2: 'Map', arg3: 'Vec2f'):
        """public void dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.write(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.lang.Integer, dev.ultreon.quantum.client.model.blockbench.BBTexture>,java.util.Map<dev.ultreon.quantum.client.model.blockbench.BBTexture, com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder>,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__BBModelMeshFace, self).write(arg0, arg1, arg2, arg3)

 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelLoader
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
from builtins import type
import dev.ultreon.quantum.client.model.blockbench.BBModelLoader as __BBModelLoader
__BBModelLoader = __BBModelLoader
import dev.ultreon.quantum.client.model.blockbench.BBModelElement as __BBModelElement
__BBModelElement = __BBModelElement
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import com.badlogic.gdx.graphics.g3d.Model as __Model
__Model = __Model
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import dev.ultreon.quantum.client.model.blockbench.BBMeta as __BBMeta
__BBMeta = __BBMeta
import dev.ultreon.quantum.client.model.blockbench.BBModelOutliner as __BBModelOutliner
__BBModelOutliner = __BBModelOutliner
import dev.ultreon.libs.commons.v0.vector.Vec3f as __Vec3f
__Vec3f = __Vec3f
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.util.List as List
from builtins import int
 
class BBModelLoader():
    """dev.ultreon.quantum.client.model.blockbench.BBModelLoader"""
 
    @staticmethod
    def __wrap(java_value: __BBModelLoader) -> 'BBModelLoader':
        return BBModelLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBModelLoader):
        """
        Dynamic initializer for BBModelLoader.
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
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getId()"""
        return 'util.Identifier'.__wrap(super(BBModelLoader, self).getId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getAnimations(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation> dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getAnimations()"""
        return 'List'.__wrap(super(BBModelLoader, self).getAnimations())

    @overload
    def getModelIdentifier(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getModelIdentifier()"""
        return str.__wrap(super(BBModelLoader, self).getModelIdentifier())

    @overload
    def getVisibleBox(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getVisibleBox()"""
        return 'vector.Vec3f'.__wrap(super(BBModelLoader, self).getVisibleBox())

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelLoader(dev.ultreon.quantum.util.Identifier)"""
        val = __BBModelLoader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMeta(self) -> 'BBMeta':
        """public dev.ultreon.quantum.client.model.blockbench.BBMeta dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getMeta()"""
        return 'BBMeta'.__wrap(super(BBModelLoader, self).getMeta())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getElements(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelElement> dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getElements()"""
        return 'List'.__wrap(super(BBModelLoader, self).getElements())

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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getName()"""
        return str.__wrap(super(BBModelLoader, self).getName())

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
    def __init__(self, arg0: 'Identifier', arg1: 'Resource'):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelLoader(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.resources.Resource)"""
        val = __BBModelLoader(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def createModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.blockbench.BBModelLoader.createModel()"""
        return 'g3d.Model'.__wrap(super(BBModelLoader, self).createModel())

    @overload
    def getOutliner(self) -> 'BBModelOutliner':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelOutliner dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getOutliner()"""
        return 'BBModelOutliner'.__wrap(super(BBModelLoader, self).getOutliner())

    @overload
    def getResolution(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getResolution()"""
        return 'vector.Vec2f'.__wrap(super(BBModelLoader, self).getResolution())

    @overload
    def getElement(self, arg0: 'UUID') -> 'BBModelElement':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelElement dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getElement(java.util.UUID)"""
        return 'BBModelElement'.__wrap(super(__BBModelLoader, self).getElement(arg0))

    @override
    @overload
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getModel()"""
        return 'g3d.Model'.__wrap(super(BBModelLoader, self).getModel())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelOutliner
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.model.blockbench.BBModelOutliner as __BBModelOutliner
__BBModelOutliner = __BBModelOutliner
import dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo as __BBModelOutlineInfo
__BBModelOutlineInfo = __BBModelOutlineInfo
import java.util.List as __List
__List = __List
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
import java.util.List as List
 
class BBModelOutliner():
    """dev.ultreon.quantum.client.model.blockbench.BBModelOutliner"""
 
    @staticmethod
    def __wrap(java_value: __BBModelOutliner) -> 'BBModelOutliner':
        return BBModelOutliner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBModelOutliner):
        """
        Dynamic initializer for BBModelOutliner.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelOutliner.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBModelOutliner, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelOutliner.toString()"""
        return str.__wrap(super(BBModelOutliner, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelOutliner.hashCode()"""
        return int.__wrap(super(BBModelOutliner, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelOutliner(java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo>)"""
        val = __BBModelOutliner(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def parent(self, arg0: 'UUID') -> 'BBModelOutlineInfo':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo dev.ultreon.quantum.client.model.blockbench.BBModelOutliner.parent(java.util.UUID)"""
        return 'BBModelOutlineInfo'.__wrap(super(__BBModelOutliner, self).parent(arg0))

    @overload
    def entries(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo> dev.ultreon.quantum.client.model.blockbench.BBModelOutliner.entries()"""
        return 'List'.__wrap(super(BBModelOutliner, self).entries())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelElement
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.model.blockbench.BBModelElement as __BBModelElement
__BBModelElement = __BBModelElement
from abc import abstractmethod, ABC
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.model.blockbench.BBModelNode as __BBModelNode
__BBModelNode = __BBModelNode
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class BBModelElement(ABC):
    """dev.ultreon.quantum.client.model.blockbench.BBModelElement"""
 
    @staticmethod
    def __wrap(java_value: __BBModelElement) -> 'BBModelElement':
        return BBModelElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBModelElement):
        """
        Dynamic initializer for BBModelElement.
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

    @abstractmethod
    def write(self, arg0: 'ModelBuilder', arg1: 'Map', arg2: 'Map', arg3: 'BBModelLoader', arg4: 'Vec2f'):
        """public abstract com.badlogic.gdx.graphics.g3d.model.Node dev.ultreon.quantum.client.model.blockbench.BBModelElement.write(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.util.UUID, com.badlogic.gdx.graphics.g3d.utils.ModelBuilder>,java.util.Map<java.lang.Integer, dev.ultreon.quantum.client.model.blockbench.BBTexture>,dev.ultreon.quantum.client.model.blockbench.BBModelLoader,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def allowMirrorModeling(self, ):
        """public abstract boolean dev.ultreon.quantum.client.model.blockbench.BBModelElement.allowMirrorModeling()"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def origin(self, ):
        """public abstract dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBModelElement.origin()"""
        pass

    @abstractmethod
    def renderOrder(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelElement.renderOrder()"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def parent(self) -> 'BBModelNode':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelNode dev.ultreon.quantum.client.model.blockbench.BBModelElement.parent()"""
        return 'BBModelNode'.__wrap(super(BBModelElement, self).parent())

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

    @abstractmethod
    def name(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelElement.name()"""
        pass

    @abstractmethod
    def uuid(self, ):
        """public abstract java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBModelElement.uuid()"""
        pass

    @override
    @overload
    def rotationMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.model.blockbench.BBModelElement.rotationMatrix()"""
        return 'math.Matrix4'.__wrap(super(BBModelElement, self).rotationMatrix())

    @abstractmethod
    def locked(self, ):
        """public abstract boolean dev.ultreon.quantum.client.model.blockbench.BBModelElement.locked()"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelElement()"""
        val = __BBModelElement()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def rotation(self, ):
        """public abstract dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBModelElement.rotation()"""
        pass

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelElement()"""
        val = __BBModelElement()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def color(self, ):
        """public abstract dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.model.blockbench.BBModelElement.color()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBColor
import dev.ultreon.quantum.client.model.blockbench.BBColor as __BBColor
__BBColor = __BBColor
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
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class BBColor():
    """dev.ultreon.quantum.client.model.blockbench.BBColor"""
 
    @staticmethod
    def __wrap(java_value: __BBColor) -> 'BBColor':
        return BBColor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBColor):
        """
        Dynamic initializer for BBColor.
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
 
    # public static final dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.BLACK
    BLACK: 'BBColor' = __wrap(__BBColor.BLACK)

    # public static final dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.GRAY
    GRAY: 'BBColor' = __wrap(__BBColor.GRAY)

    # public static final dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.CYAN
    CYAN: 'BBColor' = __wrap(__BBColor.CYAN)

    # public static final dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.YELLOW
    YELLOW: 'BBColor' = __wrap(__BBColor.YELLOW)

    # public static final dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.BROWN
    BROWN: 'BBColor' = __wrap(__BBColor.BROWN)

    # public static final dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.LIGHT_GRAY
    LIGHT_GRAY: 'BBColor' = __wrap(__BBColor.LIGHT_GRAY)

    # public static final dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.ORANGE
    ORANGE: 'BBColor' = __wrap(__BBColor.ORANGE)

    # public static final dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.WHITE
    WHITE: 'BBColor' = __wrap(__BBColor.WHITE)

    # public static final dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.PINK
    PINK: 'BBColor' = __wrap(__BBColor.PINK)

    # public static final dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.PURPLE
    PURPLE: 'BBColor' = __wrap(__BBColor.PURPLE)

    # public static final dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.RED
    RED: 'BBColor' = __wrap(__BBColor.RED)

    # public static final dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.GREEN
    GREEN: 'BBColor' = __wrap(__BBColor.GREEN)

    # public static final dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.BLUE
    BLUE: 'BBColor' = __wrap(__BBColor.BLUE)


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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BBColor':
        """public static dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.valueOf(java.lang.String)"""
        return BBColor.__wrap(__BBColor.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def values() -> List['BBColor']:
        """public static dev.ultreon.quantum.client.model.blockbench.BBColor[] dev.ultreon.quantum.client.model.blockbench.BBColor.values()"""
        return List[BBColor].__wrap(__BBColor.values())

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
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelGroup
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
import java.lang.Boolean as __boolean
from builtins import type
import dev.ultreon.quantum.client.model.blockbench.BBModelLoader as __BBModelLoader
__BBModelLoader = __BBModelLoader
import dev.ultreon.quantum.client.model.blockbench.BBModelElement as __BBModelElement
__BBModelElement = __BBModelElement
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.client.model.blockbench.BBModelNode as __BBModelNode
__BBModelNode = __BBModelNode
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
import dev.ultreon.quantum.util.RgbColor as __RgbColor
__RgbColor = __RgbColor
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec3f as __Vec3f
__Vec3f = __Vec3f
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import dev.ultreon.quantum.client.model.blockbench.BBModelGroup as __BBModelGroup
__BBModelGroup = __BBModelGroup
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
 
class BBModelGroup():
    """dev.ultreon.quantum.client.model.blockbench.BBModelGroup"""
 
    @staticmethod
    def __wrap(java_value: __BBModelGroup) -> 'BBModelGroup':
        return BBModelGroup(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBModelGroup):
        """
        Dynamic initializer for BBModelGroup.
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
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelGroup.toString()"""
        return str.__wrap(super(BBModelGroup, self).toString())

    @overload
    def children(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo> dev.ultreon.quantum.client.model.blockbench.BBModelGroup.children()"""
        return 'List'.__wrap(super(BBModelGroup, self).children())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def autouv(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelGroup.autouv()"""
        return int.__wrap(super(BBModelGroup, self).autouv())

    @overload
    def export(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelGroup.export()"""
        return bool.__wrap(super(BBModelGroup, self).export())

    @override
    @overload
    def rotationMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.model.blockbench.BBModelGroup.rotationMatrix()"""
        return 'math.Matrix4'.__wrap(super(BBModelGroup, self).rotationMatrix())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelGroup.hashCode()"""
        return int.__wrap(super(BBModelGroup, self).hashCode())

    @overload
    def element(self) -> 'BBModelElement':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelElement dev.ultreon.quantum.client.model.blockbench.BBModelGroup.element()"""
        return 'BBModelElement'.__wrap(super(BBModelGroup, self).element())

    @overload
    def __init__(self, arg0: 'BBModelLoader', arg1: str, arg2: 'Vec3f', arg3: 'RgbColor', arg4: 'UUID', arg5: bool, arg6: bool, arg7: bool, arg8: bool, arg9: int, arg10: 'List', arg11: 'Vec3f'):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelGroup(dev.ultreon.quantum.client.model.blockbench.BBModelLoader,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.quantum.util.RgbColor,java.util.UUID,boolean,boolean,boolean,boolean,int,java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo>,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        val = __BBModelGroup(arg0, arg1, arg2, arg3, arg4, __boolean.valueOf(arg5), __boolean.valueOf(arg6), __boolean.valueOf(arg7), __boolean.valueOf(arg8), __int.valueOf(arg9), arg10, arg11)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def parent(self) -> 'BBModelNode':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelNode dev.ultreon.quantum.client.model.blockbench.BBModelGroup.parent()"""
        return 'BBModelNode'.__wrap(super(BBModelGroup, self).parent())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def origin(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBModelGroup.origin()"""
        return 'vector.Vec3f'.__wrap(super(BBModelGroup, self).origin())

    @overload
    def model(self) -> 'BBModelLoader':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelLoader dev.ultreon.quantum.client.model.blockbench.BBModelGroup.model()"""
        return 'BBModelLoader'.__wrap(super(BBModelGroup, self).model())

    @override
    @overload
    def rotation(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBModelGroup.rotation()"""
        return 'vector.Vec3f'.__wrap(super(BBModelGroup, self).rotation())

    @overload
    def color(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.model.blockbench.BBModelGroup.color()"""
        return 'util.RgbColor'.__wrap(super(BBModelGroup, self).color())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelGroup.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBModelGroup, self).equals(arg0))

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelGroup.name()"""
        return str.__wrap(super(BBModelGroup, self).name())

    @overload
    def mirrorUV(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelGroup.mirrorUV()"""
        return bool.__wrap(super(BBModelGroup, self).mirrorUV())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def visibility(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelGroup.visibility()"""
        return bool.__wrap(super(BBModelGroup, self).visibility())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBModelGroup.uuid()"""
        return 'UUID'.__wrap(super(BBModelGroup, self).uuid())

    @overload
    def isOpen(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelGroup.isOpen()"""
        return bool.__wrap(super(BBModelGroup, self).isOpen())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelElementReference
import dev.ultreon.quantum.client.model.blockbench.BBModelElementReference as __BBModelElementReference
__BBModelElementReference = __BBModelElementReference
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BBModelElementReference():
    """dev.ultreon.quantum.client.model.blockbench.BBModelElementReference"""
 
    @staticmethod
    def __wrap(java_value: __BBModelElementReference) -> 'BBModelElementReference':
        return BBModelElementReference(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBModelElementReference):
        """
        Dynamic initializer for BBModelElementReference.
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
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelElementReference.hashCode()"""
        return int.__wrap(super(BBModelElementReference, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelElementReference.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBModelElementReference, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBModelElementReference.uuid()"""
        return 'UUID'.__wrap(super(BBModelElementReference, self).uuid())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'UUID'):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelElementReference(java.util.UUID)"""
        val = __BBModelElementReference(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelElementReference.toString()"""
        return str.__wrap(super(BBModelElementReference, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelFormat
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
import dev.ultreon.quantum.client.model.blockbench.BBModelFormat as __BBModelFormat
__BBModelFormat = __BBModelFormat
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class BBModelFormat():
    """dev.ultreon.quantum.client.model.blockbench.BBModelFormat"""
 
    @staticmethod
    def __wrap(java_value: __BBModelFormat) -> 'BBModelFormat':
        return BBModelFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBModelFormat):
        """
        Dynamic initializer for BBModelFormat.
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
 
    # public static final dev.ultreon.quantum.client.model.blockbench.BBModelFormat dev.ultreon.quantum.client.model.blockbench.BBModelFormat.FREE
    FREE: 'BBModelFormat' = __wrap(__BBModelFormat.FREE)


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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BBModelFormat':
        """public static dev.ultreon.quantum.client.model.blockbench.BBModelFormat dev.ultreon.quantum.client.model.blockbench.BBModelFormat.valueOf(java.lang.String)"""
        return BBModelFormat.__wrap(__BBModelFormat.valueOf(arg0))

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
    def values() -> List['BBModelFormat']:
        """public static dev.ultreon.quantum.client.model.blockbench.BBModelFormat[] dev.ultreon.quantum.client.model.blockbench.BBModelFormat.values()"""
        return List[BBModelFormat].__wrap(__BBModelFormat.values()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
import java.lang.Boolean as __boolean
from builtins import type
import dev.ultreon.quantum.client.model.blockbench.BBModelElement as __BBModelElement
__BBModelElement = __BBModelElement
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import com.badlogic.gdx.graphics.g3d.model.Node as __Node
__Node = __Node
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.client.model.blockbench.BBModelNode as __BBModelNode
__BBModelNode = __BBModelNode
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
import dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement as __BBCubeModelElement
__BBCubeModelElement = __BBCubeModelElement
from builtins import str
import dev.ultreon.quantum.util.RgbColor as __RgbColor
__RgbColor = __RgbColor
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3f as __Vec3f
__Vec3f = __Vec3f
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = __import_once__("pygdx.graphics.g3d.model")

import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
import java.util.List as List
 
class BBCubeModelElement():
    """dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement"""
 
    @staticmethod
    def __wrap(java_value: __BBCubeModelElement) -> 'BBCubeModelElement':
        return BBCubeModelElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBCubeModelElement):
        """
        Dynamic initializer for BBCubeModelElement.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBCubeModelElement, self).equals(arg0))

    @overload
    def write(self, arg0: 'ModelBuilder', arg1: 'Map', arg2: 'Map', arg3: 'BBModelLoader', arg4: 'Vec2f') -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.write(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.util.UUID, com.badlogic.gdx.graphics.g3d.utils.ModelBuilder>,java.util.Map<java.lang.Integer, dev.ultreon.quantum.client.model.blockbench.BBTexture>,dev.ultreon.quantum.client.model.blockbench.BBModelLoader,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'model.Node'.__wrap(super(__BBCubeModelElement, self).write(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: bool, arg2: bool, arg3: bool, arg4: str, arg5: bool, arg6: 'Vec3f', arg7: 'Vec3f', arg8: float, arg9: 'RgbColor', arg10: 'Vec3f', arg11: 'List', arg12: 'UUID'):
        """public dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement(java.lang.String,boolean,boolean,boolean,java.lang.String,boolean,dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f,float,dev.ultreon.quantum.util.RgbColor,dev.ultreon.libs.commons.v0.vector.Vec3f,java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelFace>,java.util.UUID)"""
        val = __BBCubeModelElement(arg0, __boolean.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3), arg4, __boolean.valueOf(arg5), arg6, arg7, __float.valueOf(arg8), arg9, arg10, arg11, arg12)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def rescale(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.rescale()"""
        return bool.__wrap(super(BBCubeModelElement, self).rescale())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.hashCode()"""
        return int.__wrap(super(BBCubeModelElement, self).hashCode())

    @override
    @overload
    def color(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.color()"""
        return 'util.RgbColor'.__wrap(super(BBCubeModelElement, self).color())

    @override
    @overload
    def locked(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.locked()"""
        return bool.__wrap(super(BBCubeModelElement, self).locked())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def to(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.to()"""
        return 'vector.Vec3f'.__wrap(super(BBCubeModelElement, self).to())

    @override
    @overload
    def rotation(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.rotation()"""
        return 'vector.Vec3f'.__wrap(super(BBCubeModelElement, self).rotation())

    @overload
    def boxUv(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.boxUv()"""
        return bool.__wrap(super(BBCubeModelElement, self).boxUv())

    @override
    @overload
    def rotationMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.rotationMatrix()"""
        return 'math.Matrix4'.__wrap(super(BBCubeModelElement, self).rotationMatrix())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.toString()"""
        return str.__wrap(super(BBCubeModelElement, self).toString())

    @overload
    def autouv(self) -> float:
        """public float dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.autouv()"""
        return float.__wrap(super(BBCubeModelElement, self).autouv())

    @override
    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.name()"""
        return str.__wrap(super(BBCubeModelElement, self).name())

    @overload
    def bake(self, arg0: 'ModelBuilder', arg1: 'Map', arg2: 'Vec2f') -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.bake(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.lang.Integer, dev.ultreon.quantum.client.model.blockbench.BBTexture>,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'model.Node'.__wrap(super(__BBCubeModelElement, self).bake(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def parent(self) -> 'BBModelNode':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelNode dev.ultreon.quantum.client.model.blockbench.BBModelElement.parent()"""
        return 'BBModelNode'.__wrap(super(BBModelElement, self).parent())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def faces(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelFace> dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.faces()"""
        return 'List'.__wrap(super(BBCubeModelElement, self).faces())

    @overload
    def from(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.from()"""
        return 'vector.Vec3f'.__wrap(super(BBCubeModelElement, self).from())

    @overload
    def __init__(self, arg0: str, arg1: bool, arg2: bool, arg3: bool, arg4: str, arg5: bool, arg6: 'Vec3f', arg7: 'Vec3f', arg8: float, arg9: 'RgbColor', arg10: 'Vec3f', arg11: 'List', arg12: 'UUID', arg13: 'Vec3f'):
        """public dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement(java.lang.String,boolean,boolean,boolean,java.lang.String,boolean,dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f,float,dev.ultreon.quantum.util.RgbColor,dev.ultreon.libs.commons.v0.vector.Vec3f,java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelFace>,java.util.UUID,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        val = __BBCubeModelElement(arg0, __boolean.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3), arg4, __boolean.valueOf(arg5), arg6, arg7, __float.valueOf(arg8), arg9, arg10, arg11, arg12, arg13)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def origin(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.origin()"""
        return 'vector.Vec3f'.__wrap(super(BBCubeModelElement, self).origin())

    @override
    @overload
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.uuid()"""
        return 'UUID'.__wrap(super(BBCubeModelElement, self).uuid())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def allowMirrorModeling(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.allowMirrorModeling()"""
        return bool.__wrap(super(BBCubeModelElement, self).allowMirrorModeling())

    @override
    @overload
    def renderOrder(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.renderOrder()"""
        return str.__wrap(super(BBCubeModelElement, self).renderOrder()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBMeta
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.model.blockbench.BBMeta as __BBMeta
__BBMeta = __BBMeta
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.model.blockbench.BBModelFormat as __BBModelFormat
__BBModelFormat = __BBModelFormat
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BBMeta():
    """dev.ultreon.quantum.client.model.blockbench.BBMeta"""
 
    @staticmethod
    def __wrap(java_value: __BBMeta) -> 'BBMeta':
        return BBMeta(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBMeta):
        """
        Dynamic initializer for BBMeta.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeta.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBMeta, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBMeta.hashCode()"""
        return int.__wrap(super(BBMeta, self).hashCode())

    @overload
    def boxUv(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeta.boxUv()"""
        return bool.__wrap(super(BBMeta, self).boxUv())

    @overload
    def modelFormat(self) -> 'BBModelFormat':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelFormat dev.ultreon.quantum.client.model.blockbench.BBMeta.modelFormat()"""
        return 'BBModelFormat'.__wrap(super(BBMeta, self).modelFormat())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: 'BBModelFormat', arg2: bool):
        """public dev.ultreon.quantum.client.model.blockbench.BBMeta(java.lang.String,dev.ultreon.quantum.client.model.blockbench.BBModelFormat,boolean)"""
        val = __BBMeta(arg0, arg1, __boolean.valueOf(arg2))
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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBMeta.toString()"""
        return str.__wrap(super(BBMeta, self).toString())

    @overload
    def formatVersion(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBMeta.formatVersion()"""
        return str.__wrap(super(BBMeta, self).formatVersion())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelOutline
import dev.ultreon.quantum.client.model.blockbench.BBModelOutline as __BBModelOutline
__BBModelOutline = __BBModelOutline
 
class BBModelOutline(ABC):
    """dev.ultreon.quantum.client.model.blockbench.BBModelOutline"""
 
    @staticmethod
    def __wrap(java_value: __BBModelOutline) -> 'BBModelOutline':
        return BBModelOutline(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBModelOutline):
        """
        Dynamic initializer for BBModelOutline.
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
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBTexture
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.net.URI as URI
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.net.URI as __URI
__URI = __URI
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.model.blockbench.BBTexture as __BBTexture
__BBTexture = __BBTexture
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class BBTexture():
    """dev.ultreon.quantum.client.model.blockbench.BBTexture"""
 
    @staticmethod
    def __wrap(java_value: __BBTexture) -> 'BBTexture':
        return BBTexture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBTexture):
        """
        Dynamic initializer for BBTexture.
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
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBTexture.uuid()"""
        return 'UUID'.__wrap(super(BBTexture, self).uuid())

    @overload
    def folder(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.folder()"""
        return str.__wrap(super(BBTexture, self).folder())

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: str, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool, arg11: str, arg12: str, arg13: str, arg14: int, arg15: str, arg16: str, arg17: bool, arg18: bool, arg19: bool, arg20: bool, arg21: 'UUID', arg22: str, arg23: 'URI'):
        """public dev.ultreon.quantum.client.model.blockbench.BBTexture(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,int,int,int,int,boolean,boolean,java.lang.String,java.lang.String,java.lang.String,int,java.lang.String,java.lang.String,boolean,boolean,boolean,boolean,java.util.UUID,java.lang.String,java.net.URI)"""
        val = __BBTexture(arg0, arg1, arg2, arg3, arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __boolean.valueOf(arg9), __boolean.valueOf(arg10), arg11, arg12, arg13, __int.valueOf(arg14), arg15, arg16, __boolean.valueOf(arg17), __boolean.valueOf(arg18), __boolean.valueOf(arg19), __boolean.valueOf(arg20), arg21, arg22, arg23)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def uvWidth(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBTexture.uvWidth()"""
        return int.__wrap(super(BBTexture, self).uvWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.toString()"""
        return str.__wrap(super(BBTexture, self).toString())

    @overload
    def saved(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.saved()"""
        return bool.__wrap(super(BBTexture, self).saved())

    @overload
    def renderSides(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.renderSides()"""
        return str.__wrap(super(BBTexture, self).renderSides())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def width(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBTexture.width()"""
        return int.__wrap(super(BBTexture, self).width())

    @overload
    def internal(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.internal()"""
        return bool.__wrap(super(BBTexture, self).internal())

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.name()"""
        return str.__wrap(super(BBTexture, self).name())

    @overload
    def frameOrder(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.frameOrder()"""
        return str.__wrap(super(BBTexture, self).frameOrder())

    @overload
    def frameInterpolate(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.frameInterpolate()"""
        return bool.__wrap(super(BBTexture, self).frameInterpolate())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBTexture, self).equals(arg0))

    @overload
    def syncToProject(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.syncToProject()"""
        return str.__wrap(super(BBTexture, self).syncToProject())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBTexture.hashCode()"""
        return int.__wrap(super(BBTexture, self).hashCode())

    @overload
    def height(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBTexture.height()"""
        return int.__wrap(super(BBTexture, self).height())

    @overload
    def particle(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.particle()"""
        return bool.__wrap(super(BBTexture, self).particle())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def path(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.path()"""
        return str.__wrap(super(BBTexture, self).path())

    @overload
    def layersEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.layersEnabled()"""
        return bool.__wrap(super(BBTexture, self).layersEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def visible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.visible()"""
        return bool.__wrap(super(BBTexture, self).visible())

    @overload
    def frameTime(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBTexture.frameTime()"""
        return int.__wrap(super(BBTexture, self).frameTime())

    @overload
    def id(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.id()"""
        return str.__wrap(super(BBTexture, self).id())

    @overload
    def renderMode(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.renderMode()"""
        return str.__wrap(super(BBTexture, self).renderMode())

    @overload
    def namespace(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.namespace()"""
        return str.__wrap(super(BBTexture, self).namespace())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def data(self) -> 'URI':
        """public java.net.URI dev.ultreon.quantum.client.model.blockbench.BBTexture.data()"""
        return 'URI'.__wrap(super(BBTexture, self).data())

    @overload
    def frameOrderType(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.frameOrderType()"""
        return str.__wrap(super(BBTexture, self).frameOrderType())

    @overload
    def relativePath(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.relativePath()"""
        return str.__wrap(super(BBTexture, self).relativePath())

    @overload
    def loadOrGetTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.model.blockbench.BBTexture.loadOrGetTexture() throws java.io.IOException"""
        return 'graphics.Texture'.__wrap(super(BBTexture, self).loadOrGetTexture())

    @overload
    def uvHeight(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBTexture.uvHeight()"""
        return int.__wrap(super(BBTexture, self).uvHeight()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelVertex
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3f as __Vec3f
__Vec3f = __Vec3f
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.model.blockbench.BBModelVertex as __BBModelVertex
__BBModelVertex = __BBModelVertex
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class BBModelVertex():
    """dev.ultreon.quantum.client.model.blockbench.BBModelVertex"""
 
    @staticmethod
    def __wrap(java_value: __BBModelVertex) -> 'BBModelVertex':
        return BBModelVertex(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBModelVertex):
        """
        Dynamic initializer for BBModelVertex.
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
 
    @overload
    def vertex(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBModelVertex.vertex()"""
        return 'vector.Vec3f'.__wrap(super(BBModelVertex, self).vertex())

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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelVertex.hashCode()"""
        return int.__wrap(super(BBModelVertex, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelVertex.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBModelVertex, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelVertex.toString()"""
        return str.__wrap(super(BBModelVertex, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Vec3f'):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelVertex(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        val = __BBModelVertex(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def write(self, arg0: 'MeshPartBuilder', arg1: 'Vec2f'):
        """public void dev.ultreon.quantum.client.model.blockbench.BBModelVertex.write(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__BBModelVertex, self).write(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelFace
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.world.CubicDirection as __CubicDirection
__CubicDirection = __CubicDirection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec4f as __Vec4f
__Vec4f = __Vec4f
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.model.blockbench.BBModelFace as __BBModelFace
__BBModelFace = __BBModelFace
from builtins import int
 
class BBModelFace():
    """dev.ultreon.quantum.client.model.blockbench.BBModelFace"""
 
    @staticmethod
    def __wrap(java_value: __BBModelFace) -> 'BBModelFace':
        return BBModelFace(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBModelFace):
        """
        Dynamic initializer for BBModelFace.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'CubicDirection', arg1: 'Vec4f', arg2: int):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelFace(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.libs.commons.v0.vector.Vec4f,int)"""
        val = __BBModelFace(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def texture(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelFace.texture()"""
        return int.__wrap(super(BBModelFace, self).texture())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelFace.toString()"""
        return str.__wrap(super(BBModelFace, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def blockFace(self) -> 'world.CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.client.model.blockbench.BBModelFace.blockFace()"""
        return 'world.CubicDirection'.__wrap(super(BBModelFace, self).blockFace())

    @overload
    def uv(self) -> 'vector.Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.quantum.client.model.blockbench.BBModelFace.uv()"""
        return 'vector.Vec4f'.__wrap(super(BBModelFace, self).uv())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelFace.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBModelFace, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelFace.hashCode()"""
        return int.__wrap(super(BBModelFace, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo as __BBModelOutlineInfo
__BBModelOutlineInfo = __BBModelOutlineInfo
 
class BBModelOutlineInfo(ABC):
    """dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo"""
 
    @staticmethod
    def __wrap(java_value: __BBModelOutlineInfo) -> 'BBModelOutlineInfo':
        return BBModelOutlineInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBModelOutlineInfo):
        """
        Dynamic initializer for BBModelOutlineInfo.
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
    def uuid(self, ):
        """public abstract java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo.uuid()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
import java.lang.Boolean as __boolean
from builtins import type
import dev.ultreon.quantum.client.model.blockbench.BBModelElement as __BBModelElement
__BBModelElement = __BBModelElement
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import com.badlogic.gdx.graphics.g3d.model.Node as __Node
__Node = __Node
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.client.model.blockbench.BBModelNode as __BBModelNode
__BBModelNode = __BBModelNode
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
import dev.ultreon.quantum.util.RgbColor as __RgbColor
__RgbColor = __RgbColor
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement as __BBMeshModelElement
__BBMeshModelElement = __BBMeshModelElement
import dev.ultreon.libs.commons.v0.vector.Vec3f as __Vec3f
__Vec3f = __Vec3f
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = __import_once__("pygdx.graphics.g3d.model")

import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
import java.util.List as List
 
class BBMeshModelElement():
    """dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement"""
 
    @staticmethod
    def __wrap(java_value: __BBMeshModelElement) -> 'BBMeshModelElement':
        return BBMeshModelElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBMeshModelElement):
        """
        Dynamic initializer for BBMeshModelElement.
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
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.name()"""
        return str.__wrap(super(BBMeshModelElement, self).name())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.toString()"""
        return str.__wrap(super(BBMeshModelElement, self).toString())

    @override
    @overload
    def renderOrder(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.renderOrder()"""
        return str.__wrap(super(BBMeshModelElement, self).renderOrder())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBMeshModelElement, self).equals(arg0))

    @overload
    def write(self, arg0: 'ModelBuilder', arg1: 'Map', arg2: 'Map', arg3: 'BBModelLoader', arg4: 'Vec2f') -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.write(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.util.UUID, com.badlogic.gdx.graphics.g3d.utils.ModelBuilder>,java.util.Map<java.lang.Integer, dev.ultreon.quantum.client.model.blockbench.BBTexture>,dev.ultreon.quantum.client.model.blockbench.BBModelLoader,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'model.Node'.__wrap(super(__BBMeshModelElement, self).write(arg0, arg1, arg2, arg3, arg4))

    @overload
    def export(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.export()"""
        return bool.__wrap(super(BBMeshModelElement, self).export())

    @override
    @overload
    def rotation(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.rotation()"""
        return 'vector.Vec3f'.__wrap(super(BBMeshModelElement, self).rotation())

    @override
    @overload
    def locked(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.locked()"""
        return bool.__wrap(super(BBMeshModelElement, self).locked())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def parent(self) -> 'BBModelNode':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelNode dev.ultreon.quantum.client.model.blockbench.BBModelElement.parent()"""
        return 'BBModelNode'.__wrap(super(BBModelElement, self).parent())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.uuid()"""
        return 'UUID'.__wrap(super(BBMeshModelElement, self).uuid())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.hashCode()"""
        return int.__wrap(super(BBMeshModelElement, self).hashCode())

    @override
    @overload
    def allowMirrorModeling(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.allowMirrorModeling()"""
        return bool.__wrap(super(BBMeshModelElement, self).allowMirrorModeling())

    @override
    @overload
    def rotationMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.model.blockbench.BBModelElement.rotationMatrix()"""
        return 'math.Matrix4'.__wrap(super(BBModelElement, self).rotationMatrix())

    @override
    @overload
    def color(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.color()"""
        return 'util.RgbColor'.__wrap(super(BBMeshModelElement, self).color())

    @override
    @overload
    def origin(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.origin()"""
        return 'vector.Vec3f'.__wrap(super(BBMeshModelElement, self).origin())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def visibility(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.visibility()"""
        return bool.__wrap(super(BBMeshModelElement, self).visibility())

    @overload
    def faces(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace> dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.faces()"""
        return 'List'.__wrap(super(BBMeshModelElement, self).faces())

    @overload
    def __init__(self, arg0: str, arg1: 'RgbColor', arg2: 'Vec3f', arg3: 'Vec3f', arg4: bool, arg5: bool, arg6: bool, arg7: str, arg8: bool, arg9: 'List', arg10: 'UUID'):
        """public dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement(java.lang.String,dev.ultreon.quantum.util.RgbColor,dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f,boolean,boolean,boolean,java.lang.String,boolean,java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace>,java.util.UUID)"""
        val = __BBMeshModelElement(arg0, arg1, arg2, arg3, __boolean.valueOf(arg4), __boolean.valueOf(arg5), __boolean.valueOf(arg6), arg7, __boolean.valueOf(arg8), arg9, arg10)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelNode
import dev.ultreon.quantum.client.model.blockbench.BBModelNode as __BBModelNode
__BBModelNode = __BBModelNode
from abc import abstractmethod, ABC
 
class BBModelNode(ABC):
    """dev.ultreon.quantum.client.model.blockbench.BBModelNode"""
 
    @staticmethod
    def __wrap(java_value: __BBModelNode) -> 'BBModelNode':
        return BBModelNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBModelNode):
        """
        Dynamic initializer for BBModelNode.
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
    def parent(self, ):
        """public abstract dev.ultreon.quantum.client.model.blockbench.BBModelNode dev.ultreon.quantum.client.model.blockbench.BBModelNode.parent()"""
        pass

    @abstractmethod
    def rotation(self, ):
        """public abstract dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBModelNode.rotation()"""
        pass

    @abstractmethod
    def uuid(self, ):
        """public abstract java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBModelNode.uuid()"""
        pass

    @abstractmethod
    def origin(self, ):
        """public abstract dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBModelNode.origin()"""
        pass

    @abstractmethod
    def rotationMatrix(self, ):
        """public abstract com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.model.blockbench.BBModelNode.rotationMatrix()"""
        pass