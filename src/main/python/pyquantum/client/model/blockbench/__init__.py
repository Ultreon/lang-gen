from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace as _BBModelMeshFace
_BBModelMeshFace = _BBModelMeshFace
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.util.List as _List
_List = _List
import java.lang.Integer as _int
from builtins import bool
import java.util.Map as Map
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class BBModelMeshFace():
    """dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace"""
 
    @staticmethod
    def _wrap(java_value: _BBModelMeshFace) -> 'BBModelMeshFace':
        return BBModelMeshFace(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBModelMeshFace):
        """
        Dynamic initializer for BBModelMeshFace.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBModelMeshFace__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBModelMeshFace__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def texture(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.texture()"""
        return int._wrap(super(BBModelMeshFace, self).texture())

    @overload
    def __init__(self, arg0: 'Map', arg1: 'List', arg2: int):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace(java.util.Map<java.lang.String, dev.ultreon.libs.commons.v0.vector.Vec2f>,java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelVertex>,int)"""
        val = _BBModelMeshFace(arg0, arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.equals(java.lang.Object)"""
        return bool._wrap(super(_BBModelMeshFace, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.hashCode()"""
        return int._wrap(super(BBModelMeshFace, self).hashCode())

    @overload
    def write(self, arg0: 'ModelBuilder', arg1: 'Map', arg2: 'Map', arg3: 'Vec2f'):
        """public void dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.write(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.lang.Integer, dev.ultreon.quantum.client.model.blockbench.BBTexture>,java.util.Map<dev.ultreon.quantum.client.model.blockbench.BBTexture, com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder>,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_BBModelMeshFace, self).write(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def vertices(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelVertex> dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.vertices()"""
        return 'List'._wrap(super(BBModelMeshFace, self).vertices())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.toString()"""
        return str._wrap(super(BBModelMeshFace, self).toString())

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
    def uvs(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.libs.commons.v0.vector.Vec2f> dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.uvs()"""
        return 'Map'._wrap(super(BBModelMeshFace, self).uvs())

 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace as _BBModelMeshFace
_BBModelMeshFace = _BBModelMeshFace
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.util.List as _List
_List = _List
import java.lang.Integer as _int
from builtins import bool
import java.util.Map as Map
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class BBModelMeshFace():
    """dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace"""
 
    @staticmethod
    def _wrap(java_value: _BBModelMeshFace) -> 'BBModelMeshFace':
        return BBModelMeshFace(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBModelMeshFace):
        """
        Dynamic initializer for BBModelMeshFace.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBModelMeshFace__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBModelMeshFace__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def texture(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.texture()"""
        return int._wrap(super(BBModelMeshFace, self).texture())

    @overload
    def __init__(self, arg0: 'Map', arg1: 'List', arg2: int):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace(java.util.Map<java.lang.String, dev.ultreon.libs.commons.v0.vector.Vec2f>,java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelVertex>,int)"""
        val = _BBModelMeshFace(arg0, arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.equals(java.lang.Object)"""
        return bool._wrap(super(_BBModelMeshFace, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.hashCode()"""
        return int._wrap(super(BBModelMeshFace, self).hashCode())

    @overload
    def write(self, arg0: 'ModelBuilder', arg1: 'Map', arg2: 'Map', arg3: 'Vec2f'):
        """public void dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.write(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.lang.Integer, dev.ultreon.quantum.client.model.blockbench.BBTexture>,java.util.Map<dev.ultreon.quantum.client.model.blockbench.BBTexture, com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder>,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_BBModelMeshFace, self).write(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def vertices(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelVertex> dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.vertices()"""
        return 'List'._wrap(super(BBModelMeshFace, self).vertices())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.toString()"""
        return str._wrap(super(BBModelMeshFace, self).toString())

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
    def uvs(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.libs.commons.v0.vector.Vec2f> dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace.uvs()"""
        return 'Map'._wrap(super(BBModelMeshFace, self).uvs())

 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelLoader
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.client.model.blockbench.BBModelLoader as _BBModelLoader
_BBModelLoader = _BBModelLoader
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.vector.Vec3f as _Vec3f
_Vec3f = _Vec3f
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.client.model.blockbench.BBModelOutliner as _BBModelOutliner
_BBModelOutliner = _BBModelOutliner
import dev.ultreon.quantum.client.model.blockbench.BBModelElement as _BBModelElement
_BBModelElement = _BBModelElement
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.vector.Vec2f as _Vec2f
_Vec2f = _Vec2f
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
import dev.ultreon.quantum.client.model.blockbench.BBMeta as _BBMeta
_BBMeta = _BBMeta
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BBModelLoader():
    """dev.ultreon.quantum.client.model.blockbench.BBModelLoader"""
 
    @staticmethod
    def _wrap(java_value: _BBModelLoader) -> 'BBModelLoader':
        return BBModelLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBModelLoader):
        """
        Dynamic initializer for BBModelLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBModelLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBModelLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getMeta(self) -> 'BBMeta':
        """public dev.ultreon.quantum.client.model.blockbench.BBMeta dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getMeta()"""
        return 'BBMeta'._wrap(super(BBModelLoader, self).getMeta())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getAnimations(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation> dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getAnimations()"""
        return 'List'._wrap(super(BBModelLoader, self).getAnimations())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getId()"""
        return 'util.Identifier'._wrap(super(BBModelLoader, self).getId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getVisibleBox(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getVisibleBox()"""
        return 'vector.Vec3f'._wrap(super(BBModelLoader, self).getVisibleBox())

    @override
    @overload
    def createModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.blockbench.BBModelLoader.createModel()"""
        return 'g3d.Model'._wrap(super(BBModelLoader, self).createModel())

    @overload
    def getModelIdentifier(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getModelIdentifier()"""
        return str._wrap(super(BBModelLoader, self).getModelIdentifier())

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
    def getOutliner(self) -> 'BBModelOutliner':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelOutliner dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getOutliner()"""
        return 'BBModelOutliner'._wrap(super(BBModelLoader, self).getOutliner())

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelLoader(dev.ultreon.quantum.util.Identifier)"""
        val = _BBModelLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getElement(self, arg0: 'UUID') -> 'BBModelElement':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelElement dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getElement(java.util.UUID)"""
        return 'BBModelElement'._wrap(super(_BBModelLoader, self).getElement(arg0))

    @override
    @overload
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getModel()"""
        return 'g3d.Model'._wrap(super(BBModelLoader, self).getModel())

    @overload
    def getElements(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelElement> dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getElements()"""
        return 'List'._wrap(super(BBModelLoader, self).getElements())

    @overload
    def getResolution(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getResolution()"""
        return 'vector.Vec2f'._wrap(super(BBModelLoader, self).getResolution())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'Resource'):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelLoader(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.resources.Resource)"""
        val = _BBModelLoader(arg0, arg1)
        self.__wrapper = val

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelLoader.getName()"""
        return str._wrap(super(BBModelLoader, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelOutliner
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.client.model.blockbench.BBModelOutliner as _BBModelOutliner
_BBModelOutliner = _BBModelOutliner
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo as _BBModelOutlineInfo
_BBModelOutlineInfo = _BBModelOutlineInfo
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class BBModelOutliner():
    """dev.ultreon.quantum.client.model.blockbench.BBModelOutliner"""
 
    @staticmethod
    def _wrap(java_value: _BBModelOutliner) -> 'BBModelOutliner':
        return BBModelOutliner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBModelOutliner):
        """
        Dynamic initializer for BBModelOutliner.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBModelOutliner__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBModelOutliner__wrapper":
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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelOutliner.toString()"""
        return str._wrap(super(BBModelOutliner, self).toString())

    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelOutliner(java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo>)"""
        val = _BBModelOutliner(arg0)
        self.__wrapper = val

    @overload
    def parent(self, arg0: 'UUID') -> 'BBModelOutlineInfo':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo dev.ultreon.quantum.client.model.blockbench.BBModelOutliner.parent(java.util.UUID)"""
        return 'BBModelOutlineInfo'._wrap(super(_BBModelOutliner, self).parent(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelOutliner.equals(java.lang.Object)"""
        return bool._wrap(super(_BBModelOutliner, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def entries(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo> dev.ultreon.quantum.client.model.blockbench.BBModelOutliner.entries()"""
        return 'List'._wrap(super(BBModelOutliner, self).entries())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelOutliner.hashCode()"""
        return int._wrap(super(BBModelOutliner, self).hashCode())

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
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelElement
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.model.blockbench.BBModelNode as _BBModelNode
_BBModelNode = _BBModelNode
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
from abc import abstractmethod, ABC
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.blockbench.BBModelElement as _BBModelElement
_BBModelElement = _BBModelElement
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import java.util.Map as Map
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BBModelElement():
    """dev.ultreon.quantum.client.model.blockbench.BBModelElement"""
 
    @staticmethod
    def _wrap(java_value: _BBModelElement) -> 'BBModelElement':
        return BBModelElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBModelElement):
        """
        Dynamic initializer for BBModelElement.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBModelElement__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBModelElement__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def write(self, arg0: 'ModelBuilder', arg1: 'Map', arg2: 'Map', arg3: 'BBModelLoader', arg4: 'Vec2f'):
        """public abstract com.badlogic.gdx.graphics.g3d.model.Node dev.ultreon.quantum.client.model.blockbench.BBModelElement.write(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.util.UUID, com.badlogic.gdx.graphics.g3d.utils.ModelBuilder>,java.util.Map<java.lang.Integer, dev.ultreon.quantum.client.model.blockbench.BBTexture>,dev.ultreon.quantum.client.model.blockbench.BBModelLoader,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def allowMirrorModeling(self, ):
        """public abstract boolean dev.ultreon.quantum.client.model.blockbench.BBModelElement.allowMirrorModeling()"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parent(self) -> 'BBModelNode':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelNode dev.ultreon.quantum.client.model.blockbench.BBModelElement.parent()"""
        return 'BBModelNode'._wrap(super(BBModelElement, self).parent())

    @override
    @overload
    def rotationMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.model.blockbench.BBModelElement.rotationMatrix()"""
        return 'math.Matrix4'._wrap(super(BBModelElement, self).rotationMatrix())

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelElement()"""
        val = _BBModelElement()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelElement()"""
        val = _BBModelElement()
        self.__wrapper = val

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def locked(self, ):
        """public abstract boolean dev.ultreon.quantum.client.model.blockbench.BBModelElement.locked()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def rotation(self, ):
        """public abstract dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBModelElement.rotation()"""
        pass

    @abstractmethod
    def color(self, ):
        """public abstract dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.model.blockbench.BBModelElement.color()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBColor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.blockbench.BBColor as _BBColor
_BBColor = _BBColor
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BBColor():
    """dev.ultreon.quantum.client.model.blockbench.BBColor"""
 
    @staticmethod
    def _wrap(java_value: _BBColor) -> 'BBColor':
        return BBColor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBColor):
        """
        Dynamic initializer for BBColor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBColor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBColor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @staticmethod
    @overload
    def values() -> List['BBColor']:
        """public static dev.ultreon.quantum.client.model.blockbench.BBColor[] dev.ultreon.quantum.client.model.blockbench.BBColor.values()"""
        return List[BBColor]._wrap(_BBColor.values())

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BBColor':
        """public static dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.BBColor.valueOf(java.lang.String)"""
        return BBColor._wrap(_BBColor.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


BBColor.CYAN = BBColor._wrap(_CYAN.CYAN)

BBColor.ORANGE = BBColor._wrap(_ORANGE.ORANGE)

BBColor.PURPLE = BBColor._wrap(_PURPLE.PURPLE)

BBColor.BROWN = BBColor._wrap(_BROWN.BROWN)

BBColor.PINK = BBColor._wrap(_PINK.PINK)

BBColor.YELLOW = BBColor._wrap(_YELLOW.YELLOW)

BBColor.RED = BBColor._wrap(_RED.RED)

BBColor.LIGHT_GRAY = BBColor._wrap(_LIGHT_GRAY.LIGHT_GRAY)

BBColor.BLACK = BBColor._wrap(_BLACK.BLACK)

BBColor.BLUE = BBColor._wrap(_BLUE.BLUE)

BBColor.GREEN = BBColor._wrap(_GREEN.GREEN)

BBColor.GRAY = BBColor._wrap(_GRAY.GRAY)

BBColor.WHITE = BBColor._wrap(_WHITE.WHITE) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelGroup
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.model.blockbench.BBModelNode as _BBModelNode
_BBModelNode = _BBModelNode
from builtins import type
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.util.RgbColor as _RgbColor
_RgbColor = _RgbColor
import java.lang.String as _string
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import dev.ultreon.quantum.client.model.blockbench.BBModelGroup as _BBModelGroup
_BBModelGroup = _BBModelGroup
from builtins import bool
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.client.model.blockbench.BBModelLoader as _BBModelLoader
_BBModelLoader = _BBModelLoader
import java.lang.Object as _object
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.vector.Vec3f as _Vec3f
_Vec3f = _Vec3f
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.client.model.blockbench.BBModelElement as _BBModelElement
_BBModelElement = _BBModelElement
import java.lang.Integer as _int
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
 
class BBModelGroup():
    """dev.ultreon.quantum.client.model.blockbench.BBModelGroup"""
 
    @staticmethod
    def _wrap(java_value: _BBModelGroup) -> 'BBModelGroup':
        return BBModelGroup(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBModelGroup):
        """
        Dynamic initializer for BBModelGroup.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBModelGroup__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBModelGroup__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBModelGroup.uuid()"""
        return 'UUID'._wrap(super(BBModelGroup, self).uuid())

    @overload
    def element(self) -> 'BBModelElement':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelElement dev.ultreon.quantum.client.model.blockbench.BBModelGroup.element()"""
        return 'BBModelElement'._wrap(super(BBModelGroup, self).element())

    @override
    @overload
    def parent(self) -> 'BBModelNode':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelNode dev.ultreon.quantum.client.model.blockbench.BBModelGroup.parent()"""
        return 'BBModelNode'._wrap(super(BBModelGroup, self).parent())

    @overload
    def model(self) -> 'BBModelLoader':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelLoader dev.ultreon.quantum.client.model.blockbench.BBModelGroup.model()"""
        return 'BBModelLoader'._wrap(super(BBModelGroup, self).model())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelGroup.hashCode()"""
        return int._wrap(super(BBModelGroup, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def rotation(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBModelGroup.rotation()"""
        return 'vector.Vec3f'._wrap(super(BBModelGroup, self).rotation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelGroup.equals(java.lang.Object)"""
        return bool._wrap(super(_BBModelGroup, self).equals(arg0))

    @overload
    def color(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.model.blockbench.BBModelGroup.color()"""
        return 'util.RgbColor'._wrap(super(BBModelGroup, self).color())

    @override
    @overload
    def origin(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBModelGroup.origin()"""
        return 'vector.Vec3f'._wrap(super(BBModelGroup, self).origin())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'BBModelLoader', arg1: str, arg2: 'Vec3f', arg3: 'RgbColor', arg4: 'UUID', arg5: bool, arg6: bool, arg7: bool, arg8: bool, arg9: int, arg10: 'List', arg11: 'Vec3f'):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelGroup(dev.ultreon.quantum.client.model.blockbench.BBModelLoader,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.quantum.util.RgbColor,java.util.UUID,boolean,boolean,boolean,boolean,int,java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo>,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        val = _BBModelGroup(arg0, arg1, arg2, arg3, arg4, _boolean.valueOf(arg5), _boolean.valueOf(arg6), _boolean.valueOf(arg7), _boolean.valueOf(arg8), _int.valueOf(arg9), arg10, arg11)
        self.__wrapper = val

    @overload
    def children(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo> dev.ultreon.quantum.client.model.blockbench.BBModelGroup.children()"""
        return 'List'._wrap(super(BBModelGroup, self).children())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelGroup.toString()"""
        return str._wrap(super(BBModelGroup, self).toString())

    @overload
    def mirrorUV(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelGroup.mirrorUV()"""
        return bool._wrap(super(BBModelGroup, self).mirrorUV())

    @overload
    def autouv(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelGroup.autouv()"""
        return int._wrap(super(BBModelGroup, self).autouv())

    @override
    @overload
    def rotationMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.model.blockbench.BBModelGroup.rotationMatrix()"""
        return 'math.Matrix4'._wrap(super(BBModelGroup, self).rotationMatrix())

    @overload
    def export(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelGroup.export()"""
        return bool._wrap(super(BBModelGroup, self).export())

    @overload
    def visibility(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelGroup.visibility()"""
        return bool._wrap(super(BBModelGroup, self).visibility())

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelGroup.name()"""
        return str._wrap(super(BBModelGroup, self).name())

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
    def isOpen(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelGroup.isOpen()"""
        return bool._wrap(super(BBModelGroup, self).isOpen()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelElementReference
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.blockbench.BBModelElementReference as _BBModelElementReference
_BBModelElementReference = _BBModelElementReference
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
 
class BBModelElementReference():
    """dev.ultreon.quantum.client.model.blockbench.BBModelElementReference"""
 
    @staticmethod
    def _wrap(java_value: _BBModelElementReference) -> 'BBModelElementReference':
        return BBModelElementReference(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBModelElementReference):
        """
        Dynamic initializer for BBModelElementReference.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBModelElementReference__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBModelElementReference__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelElementReference.toString()"""
        return str._wrap(super(BBModelElementReference, self).toString())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelElementReference.equals(java.lang.Object)"""
        return bool._wrap(super(_BBModelElementReference, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelElementReference.hashCode()"""
        return int._wrap(super(BBModelElementReference, self).hashCode())

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
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBModelElementReference.uuid()"""
        return 'UUID'._wrap(super(BBModelElementReference, self).uuid())

    @overload
    def __init__(self, arg0: 'UUID'):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelElementReference(java.util.UUID)"""
        val = _BBModelElementReference(arg0)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelFormat
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
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.blockbench.BBModelFormat as _BBModelFormat
_BBModelFormat = _BBModelFormat
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BBModelFormat():
    """dev.ultreon.quantum.client.model.blockbench.BBModelFormat"""
 
    @staticmethod
    def _wrap(java_value: _BBModelFormat) -> 'BBModelFormat':
        return BBModelFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBModelFormat):
        """
        Dynamic initializer for BBModelFormat.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBModelFormat__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBModelFormat__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BBModelFormat':
        """public static dev.ultreon.quantum.client.model.blockbench.BBModelFormat dev.ultreon.quantum.client.model.blockbench.BBModelFormat.valueOf(java.lang.String)"""
        return BBModelFormat._wrap(_BBModelFormat.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['BBModelFormat']:
        """public static dev.ultreon.quantum.client.model.blockbench.BBModelFormat[] dev.ultreon.quantum.client.model.blockbench.BBModelFormat.values()"""
        return List[BBModelFormat]._wrap(_BBModelFormat.values())

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


BBModelFormat.FREE = BBModelFormat._wrap(_FREE.FREE) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.model.blockbench.BBModelNode as _BBModelNode
_BBModelNode = _BBModelNode
from builtins import type
import dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement as _BBCubeModelElement
_BBCubeModelElement = _BBCubeModelElement
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.util.RgbColor as _RgbColor
_RgbColor = _RgbColor
import java.lang.String as _string
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g3d.model.Node as _Node
_Node = _Node
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.vector.Vec3f as _Vec3f
_Vec3f = _Vec3f
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
import dev.ultreon.quantum.client.model.blockbench.BBModelElement as _BBModelElement
_BBModelElement = _BBModelElement
import java.lang.Integer as _int
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = _import_once("pygdx.graphics.g3d.model")

import java.util.Map as Map
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class BBCubeModelElement():
    """dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement"""
 
    @staticmethod
    def _wrap(java_value: _BBCubeModelElement) -> 'BBCubeModelElement':
        return BBCubeModelElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBCubeModelElement):
        """
        Dynamic initializer for BBCubeModelElement.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBCubeModelElement__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBCubeModelElement__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def locked(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.locked()"""
        return bool._wrap(super(BBCubeModelElement, self).locked())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def from(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.from()"""
        return 'vector.Vec3f'._wrap(super(BBCubeModelElement, self).from())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.toString()"""
        return str._wrap(super(BBCubeModelElement, self).toString())

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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.hashCode()"""
        return int._wrap(super(BBCubeModelElement, self).hashCode())

    @overload
    def bake(self, arg0: 'ModelBuilder', arg1: 'Map', arg2: 'Vec2f') -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.bake(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.lang.Integer, dev.ultreon.quantum.client.model.blockbench.BBTexture>,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'model.Node'._wrap(super(_BBCubeModelElement, self).bake(arg0, arg1, arg2))

    @overload
    def write(self, arg0: 'ModelBuilder', arg1: 'Map', arg2: 'Map', arg3: 'BBModelLoader', arg4: 'Vec2f') -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.write(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.util.UUID, com.badlogic.gdx.graphics.g3d.utils.ModelBuilder>,java.util.Map<java.lang.Integer, dev.ultreon.quantum.client.model.blockbench.BBTexture>,dev.ultreon.quantum.client.model.blockbench.BBModelLoader,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'model.Node'._wrap(super(_BBCubeModelElement, self).write(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def rotation(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.rotation()"""
        return 'vector.Vec3f'._wrap(super(BBCubeModelElement, self).rotation())

    @override
    @overload
    def color(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.color()"""
        return 'util.RgbColor'._wrap(super(BBCubeModelElement, self).color())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.equals(java.lang.Object)"""
        return bool._wrap(super(_BBCubeModelElement, self).equals(arg0))

    @overload
    def faces(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelFace> dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.faces()"""
        return 'List'._wrap(super(BBCubeModelElement, self).faces())

    @overload
    def rescale(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.rescale()"""
        return bool._wrap(super(BBCubeModelElement, self).rescale())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def parent(self) -> 'BBModelNode':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelNode dev.ultreon.quantum.client.model.blockbench.BBModelElement.parent()"""
        return 'BBModelNode'._wrap(super(BBModelElement, self).parent())

    @overload
    def __init__(self, arg0: str, arg1: bool, arg2: bool, arg3: bool, arg4: str, arg5: bool, arg6: 'Vec3f', arg7: 'Vec3f', arg8: float, arg9: 'RgbColor', arg10: 'Vec3f', arg11: 'List', arg12: 'UUID'):
        """public dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement(java.lang.String,boolean,boolean,boolean,java.lang.String,boolean,dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f,float,dev.ultreon.quantum.util.RgbColor,dev.ultreon.libs.commons.v0.vector.Vec3f,java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelFace>,java.util.UUID)"""
        val = _BBCubeModelElement(arg0, _boolean.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3), arg4, _boolean.valueOf(arg5), arg6, arg7, _float.valueOf(arg8), arg9, arg10, arg11, arg12)
        self.__wrapper = val

    @override
    @overload
    def renderOrder(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.renderOrder()"""
        return str._wrap(super(BBCubeModelElement, self).renderOrder())

    @override
    @overload
    def rotationMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.rotationMatrix()"""
        return 'math.Matrix4'._wrap(super(BBCubeModelElement, self).rotationMatrix())

    @overload
    def autouv(self) -> float:
        """public float dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.autouv()"""
        return float._wrap(super(BBCubeModelElement, self).autouv())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def allowMirrorModeling(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.allowMirrorModeling()"""
        return bool._wrap(super(BBCubeModelElement, self).allowMirrorModeling())

    @override
    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.name()"""
        return str._wrap(super(BBCubeModelElement, self).name())

    @overload
    def to(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.to()"""
        return 'vector.Vec3f'._wrap(super(BBCubeModelElement, self).to())

    @overload
    def boxUv(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.boxUv()"""
        return bool._wrap(super(BBCubeModelElement, self).boxUv())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def origin(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.origin()"""
        return 'vector.Vec3f'._wrap(super(BBCubeModelElement, self).origin())

    @overload
    def __init__(self, arg0: str, arg1: bool, arg2: bool, arg3: bool, arg4: str, arg5: bool, arg6: 'Vec3f', arg7: 'Vec3f', arg8: float, arg9: 'RgbColor', arg10: 'Vec3f', arg11: 'List', arg12: 'UUID', arg13: 'Vec3f'):
        """public dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement(java.lang.String,boolean,boolean,boolean,java.lang.String,boolean,dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f,float,dev.ultreon.quantum.util.RgbColor,dev.ultreon.libs.commons.v0.vector.Vec3f,java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelFace>,java.util.UUID,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        val = _BBCubeModelElement(arg0, _boolean.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3), arg4, _boolean.valueOf(arg5), arg6, arg7, _float.valueOf(arg8), arg9, arg10, arg11, arg12, arg13)
        self.__wrapper = val

    @override
    @overload
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBCubeModelElement.uuid()"""
        return 'UUID'._wrap(super(BBCubeModelElement, self).uuid()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBMeta
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.blockbench.BBModelFormat as _BBModelFormat
_BBModelFormat = _BBModelFormat
import dev.ultreon.quantum.client.model.blockbench.BBMeta as _BBMeta
_BBMeta = _BBMeta
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BBMeta():
    """dev.ultreon.quantum.client.model.blockbench.BBMeta"""
 
    @staticmethod
    def _wrap(java_value: _BBMeta) -> 'BBMeta':
        return BBMeta(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBMeta):
        """
        Dynamic initializer for BBMeta.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBMeta__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBMeta__wrapper":
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
    def boxUv(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeta.boxUv()"""
        return bool._wrap(super(BBMeta, self).boxUv())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def modelFormat(self) -> 'BBModelFormat':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelFormat dev.ultreon.quantum.client.model.blockbench.BBMeta.modelFormat()"""
        return 'BBModelFormat'._wrap(super(BBMeta, self).modelFormat())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBMeta.hashCode()"""
        return int._wrap(super(BBMeta, self).hashCode())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBMeta.toString()"""
        return str._wrap(super(BBMeta, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeta.equals(java.lang.Object)"""
        return bool._wrap(super(_BBMeta, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def formatVersion(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBMeta.formatVersion()"""
        return str._wrap(super(BBMeta, self).formatVersion())

    @overload
    def __init__(self, arg0: str, arg1: 'BBModelFormat', arg2: bool):
        """public dev.ultreon.quantum.client.model.blockbench.BBMeta(java.lang.String,dev.ultreon.quantum.client.model.blockbench.BBModelFormat,boolean)"""
        val = _BBMeta(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelOutline
import dev.ultreon.quantum.client.model.blockbench.BBModelOutline as _BBModelOutline
_BBModelOutline = _BBModelOutline
 
class BBModelOutline():
    """dev.ultreon.quantum.client.model.blockbench.BBModelOutline"""
 
    @staticmethod
    def _wrap(java_value: _BBModelOutline) -> 'BBModelOutline':
        return BBModelOutline(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBModelOutline):
        """
        Dynamic initializer for BBModelOutline.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBModelOutline__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBModelOutline__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__)) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBTexture
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.net.URI as _URI
_URI = _URI
import java.util.UUID as UUID
from pyquantum_helper import override
import java.net.URI as URI
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.blockbench.BBTexture as _BBTexture
_BBTexture = _BBTexture
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
 
class BBTexture():
    """dev.ultreon.quantum.client.model.blockbench.BBTexture"""
 
    @staticmethod
    def _wrap(java_value: _BBTexture) -> 'BBTexture':
        return BBTexture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBTexture):
        """
        Dynamic initializer for BBTexture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBTexture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBTexture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def path(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.path()"""
        return str._wrap(super(BBTexture, self).path())

    @overload
    def data(self) -> 'URI':
        """public java.net.URI dev.ultreon.quantum.client.model.blockbench.BBTexture.data()"""
        return 'URI'._wrap(super(BBTexture, self).data())

    @overload
    def uvWidth(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBTexture.uvWidth()"""
        return int._wrap(super(BBTexture, self).uvWidth())

    @overload
    def particle(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.particle()"""
        return bool._wrap(super(BBTexture, self).particle())

    @overload
    def height(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBTexture.height()"""
        return int._wrap(super(BBTexture, self).height())

    @overload
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBTexture.uuid()"""
        return 'UUID'._wrap(super(BBTexture, self).uuid())

    @overload
    def syncToProject(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.syncToProject()"""
        return str._wrap(super(BBTexture, self).syncToProject())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def saved(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.saved()"""
        return bool._wrap(super(BBTexture, self).saved())

    @overload
    def id(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.id()"""
        return str._wrap(super(BBTexture, self).id())

    @overload
    def namespace(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.namespace()"""
        return str._wrap(super(BBTexture, self).namespace())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.toString()"""
        return str._wrap(super(BBTexture, self).toString())

    @overload
    def loadOrGetTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.model.blockbench.BBTexture.loadOrGetTexture() throws java.io.IOException"""
        return 'graphics.Texture'._wrap(super(BBTexture, self).loadOrGetTexture())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def renderSides(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.renderSides()"""
        return str._wrap(super(BBTexture, self).renderSides())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def folder(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.folder()"""
        return str._wrap(super(BBTexture, self).folder())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBTexture.hashCode()"""
        return int._wrap(super(BBTexture, self).hashCode())

    @overload
    def uvHeight(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBTexture.uvHeight()"""
        return int._wrap(super(BBTexture, self).uvHeight())

    @overload
    def width(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBTexture.width()"""
        return int._wrap(super(BBTexture, self).width())

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: str, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool, arg11: str, arg12: str, arg13: str, arg14: int, arg15: str, arg16: str, arg17: bool, arg18: bool, arg19: bool, arg20: bool, arg21: 'UUID', arg22: str, arg23: 'URI'):
        """public dev.ultreon.quantum.client.model.blockbench.BBTexture(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,int,int,int,int,boolean,boolean,java.lang.String,java.lang.String,java.lang.String,int,java.lang.String,java.lang.String,boolean,boolean,boolean,boolean,java.util.UUID,java.lang.String,java.net.URI)"""
        val = _BBTexture(arg0, arg1, arg2, arg3, arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _boolean.valueOf(arg9), _boolean.valueOf(arg10), arg11, arg12, arg13, _int.valueOf(arg14), arg15, arg16, _boolean.valueOf(arg17), _boolean.valueOf(arg18), _boolean.valueOf(arg19), _boolean.valueOf(arg20), arg21, arg22, arg23)
        self.__wrapper = val

    @overload
    def internal(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.internal()"""
        return bool._wrap(super(BBTexture, self).internal())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.name()"""
        return str._wrap(super(BBTexture, self).name())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.equals(java.lang.Object)"""
        return bool._wrap(super(_BBTexture, self).equals(arg0))

    @overload
    def visible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.visible()"""
        return bool._wrap(super(BBTexture, self).visible())

    @overload
    def frameTime(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBTexture.frameTime()"""
        return int._wrap(super(BBTexture, self).frameTime())

    @overload
    def renderMode(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.renderMode()"""
        return str._wrap(super(BBTexture, self).renderMode())

    @overload
    def frameOrderType(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.frameOrderType()"""
        return str._wrap(super(BBTexture, self).frameOrderType())

    @overload
    def relativePath(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.relativePath()"""
        return str._wrap(super(BBTexture, self).relativePath())

    @overload
    def frameOrder(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBTexture.frameOrder()"""
        return str._wrap(super(BBTexture, self).frameOrder())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def frameInterpolate(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.frameInterpolate()"""
        return bool._wrap(super(BBTexture, self).frameInterpolate())

    @overload
    def layersEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBTexture.layersEnabled()"""
        return bool._wrap(super(BBTexture, self).layersEnabled())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelVertex
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.model.blockbench.BBModelVertex as _BBModelVertex
_BBModelVertex = _BBModelVertex
import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.libs.commons.v0.vector.Vec3f as _Vec3f
_Vec3f = _Vec3f
import java.lang.Integer as _int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BBModelVertex():
    """dev.ultreon.quantum.client.model.blockbench.BBModelVertex"""
 
    @staticmethod
    def _wrap(java_value: _BBModelVertex) -> 'BBModelVertex':
        return BBModelVertex(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBModelVertex):
        """
        Dynamic initializer for BBModelVertex.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBModelVertex__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBModelVertex__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelVertex.toString()"""
        return str._wrap(super(BBModelVertex, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def vertex(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBModelVertex.vertex()"""
        return 'vector.Vec3f'._wrap(super(BBModelVertex, self).vertex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def write(self, arg0: 'MeshPartBuilder', arg1: 'Vec2f'):
        """public void dev.ultreon.quantum.client.model.blockbench.BBModelVertex.write(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(_BBModelVertex, self).write(arg0, arg1)

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelVertex.equals(java.lang.Object)"""
        return bool._wrap(super(_BBModelVertex, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelVertex.hashCode()"""
        return int._wrap(super(BBModelVertex, self).hashCode())

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
    def __init__(self, arg0: 'Vec3f'):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelVertex(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        val = _BBModelVertex(arg0)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelFace
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.libs.commons.v0.vector.Vec4f as _Vec4f
_Vec4f = _Vec4f
import dev.ultreon.quantum.world.CubicDirection as _CubicDirection
_CubicDirection = _CubicDirection
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.blockbench.BBModelFace as _BBModelFace
_BBModelFace = _BBModelFace
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BBModelFace():
    """dev.ultreon.quantum.client.model.blockbench.BBModelFace"""
 
    @staticmethod
    def _wrap(java_value: _BBModelFace) -> 'BBModelFace':
        return BBModelFace(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBModelFace):
        """
        Dynamic initializer for BBModelFace.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBModelFace__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBModelFace__wrapper":
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
    def __init__(self, arg0: 'CubicDirection', arg1: 'Vec4f', arg2: int):
        """public dev.ultreon.quantum.client.model.blockbench.BBModelFace(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.libs.commons.v0.vector.Vec4f,int)"""
        val = _BBModelFace(arg0, arg1, _int.valueOf(arg2))
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

    @overload
    def texture(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelFace.texture()"""
        return int._wrap(super(BBModelFace, self).texture())

    @overload
    def uv(self) -> 'vector.Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.quantum.client.model.blockbench.BBModelFace.uv()"""
        return 'vector.Vec4f'._wrap(super(BBModelFace, self).uv())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBModelFace.hashCode()"""
        return int._wrap(super(BBModelFace, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBModelFace.toString()"""
        return str._wrap(super(BBModelFace, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBModelFace.equals(java.lang.Object)"""
        return bool._wrap(super(_BBModelFace, self).equals(arg0))

    @overload
    def blockFace(self) -> 'world.CubicDirection':
        """public dev.ultreon.quantum.world.CubicDirection dev.ultreon.quantum.client.model.blockbench.BBModelFace.blockFace()"""
        return 'world.CubicDirection'._wrap(super(BBModelFace, self).blockFace()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo as _BBModelOutlineInfo
_BBModelOutlineInfo = _BBModelOutlineInfo
 
class BBModelOutlineInfo():
    """dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo"""
 
    @staticmethod
    def _wrap(java_value: _BBModelOutlineInfo) -> 'BBModelOutlineInfo':
        return BBModelOutlineInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBModelOutlineInfo):
        """
        Dynamic initializer for BBModelOutlineInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBModelOutlineInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBModelOutlineInfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def uuid(self, ):
        """public abstract java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBModelOutlineInfo.uuid()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.model.blockbench.BBModelNode as _BBModelNode
_BBModelNode = _BBModelNode
from builtins import type
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.util.RgbColor as _RgbColor
_RgbColor = _RgbColor
import java.lang.String as _string
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g3d.model.Node as _Node
_Node = _Node
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.vector.Vec3f as _Vec3f
_Vec3f = _Vec3f
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement as _BBMeshModelElement
_BBMeshModelElement = _BBMeshModelElement
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.client.model.blockbench.BBModelElement as _BBModelElement
_BBModelElement = _BBModelElement
import java.lang.Integer as _int
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = _import_once("pygdx.graphics.g3d.model")

import java.util.Map as Map
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class BBMeshModelElement():
    """dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement"""
 
    @staticmethod
    def _wrap(java_value: _BBMeshModelElement) -> 'BBMeshModelElement':
        return BBMeshModelElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBMeshModelElement):
        """
        Dynamic initializer for BBMeshModelElement.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBMeshModelElement__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBMeshModelElement__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.name()"""
        return str._wrap(super(BBMeshModelElement, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.hashCode()"""
        return int._wrap(super(BBMeshModelElement, self).hashCode())

    @overload
    def export(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.export()"""
        return bool._wrap(super(BBMeshModelElement, self).export())

    @override
    @overload
    def locked(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.locked()"""
        return bool._wrap(super(BBMeshModelElement, self).locked())

    @overload
    def __init__(self, arg0: str, arg1: 'RgbColor', arg2: 'Vec3f', arg3: 'Vec3f', arg4: bool, arg5: bool, arg6: bool, arg7: str, arg8: bool, arg9: 'List', arg10: 'UUID'):
        """public dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement(java.lang.String,dev.ultreon.quantum.util.RgbColor,dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f,boolean,boolean,boolean,java.lang.String,boolean,java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace>,java.util.UUID)"""
        val = _BBMeshModelElement(arg0, arg1, arg2, arg3, _boolean.valueOf(arg4), _boolean.valueOf(arg5), _boolean.valueOf(arg6), arg7, _boolean.valueOf(arg8), arg9, arg10)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def allowMirrorModeling(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.allowMirrorModeling()"""
        return bool._wrap(super(BBMeshModelElement, self).allowMirrorModeling())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.equals(java.lang.Object)"""
        return bool._wrap(super(_BBMeshModelElement, self).equals(arg0))

    @overload
    def write(self, arg0: 'ModelBuilder', arg1: 'Map', arg2: 'Map', arg3: 'BBModelLoader', arg4: 'Vec2f') -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.write(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,java.util.Map<java.util.UUID, com.badlogic.gdx.graphics.g3d.utils.ModelBuilder>,java.util.Map<java.lang.Integer, dev.ultreon.quantum.client.model.blockbench.BBTexture>,dev.ultreon.quantum.client.model.blockbench.BBModelLoader,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'model.Node'._wrap(super(_BBMeshModelElement, self).write(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.uuid()"""
        return 'UUID'._wrap(super(BBMeshModelElement, self).uuid())

    @override
    @overload
    def parent(self) -> 'BBModelNode':
        """public dev.ultreon.quantum.client.model.blockbench.BBModelNode dev.ultreon.quantum.client.model.blockbench.BBModelElement.parent()"""
        return 'BBModelNode'._wrap(super(BBModelElement, self).parent())

    @override
    @overload
    def rotationMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 dev.ultreon.quantum.client.model.blockbench.BBModelElement.rotationMatrix()"""
        return 'math.Matrix4'._wrap(super(BBModelElement, self).rotationMatrix())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.toString()"""
        return str._wrap(super(BBMeshModelElement, self).toString())

    @override
    @overload
    def renderOrder(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.renderOrder()"""
        return str._wrap(super(BBMeshModelElement, self).renderOrder())

    @override
    @overload
    def origin(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.origin()"""
        return 'vector.Vec3f'._wrap(super(BBMeshModelElement, self).origin())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def color(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.color()"""
        return 'util.RgbColor'._wrap(super(BBMeshModelElement, self).color())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def faces(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.BBModelMeshFace> dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.faces()"""
        return 'List'._wrap(super(BBMeshModelElement, self).faces())

    @override
    @overload
    def rotation(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.rotation()"""
        return 'vector.Vec3f'._wrap(super(BBMeshModelElement, self).rotation())

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
    def visibility(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.BBMeshModelElement.visibility()"""
        return bool._wrap(super(BBMeshModelElement, self).visibility()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.BBModelNode
import dev.ultreon.quantum.client.model.blockbench.BBModelNode as _BBModelNode
_BBModelNode = _BBModelNode
from abc import abstractmethod, ABC
 
class BBModelNode():
    """dev.ultreon.quantum.client.model.blockbench.BBModelNode"""
 
    @staticmethod
    def _wrap(java_value: _BBModelNode) -> 'BBModelNode':
        return BBModelNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBModelNode):
        """
        Dynamic initializer for BBModelNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBModelNode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBModelNode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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