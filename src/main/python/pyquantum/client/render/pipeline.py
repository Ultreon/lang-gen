from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.render.pipeline.MainRenderNode as _MainRenderNode
_MainRenderNode = _MainRenderNode
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pyquantum.client import input
except ImportError:
    input = _import_once("pyquantum.client.input")

import java.io.PrintStream as PrintStream
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as _RenderPipeline_RenderNode
_RenderNode = _RenderPipeline_RenderNode.RenderNode
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

import com.badlogic.gdx.graphics.Mesh as _Mesh
_Mesh = _Mesh
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MainRenderNode():
    """dev.ultreon.quantum.client.render.pipeline.MainRenderNode"""
 
    @staticmethod
    def _wrap(java_value: _MainRenderNode) -> 'MainRenderNode':
        return MainRenderNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MainRenderNode):
        """
        Dynamic initializer for MainRenderNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MainRenderNode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MainRenderNode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.MainRenderNode.dumpInfo(java.io.PrintStream)"""
        super(_MainRenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.MainRenderNode.resize(int,int)"""
        super(_MainRenderNode, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.MainRenderNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'._wrap(super(_MainRenderNode, self).render(arg0, arg1, arg2, arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.MainRenderNode()"""
        val = _MainRenderNode()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dispose()"""
        super(RenderNode, self).dispose()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.MainRenderNode()"""
        val = _MainRenderNode()
        self.__wrapper = val

    @overload
    def createFullScreenQuad(self) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.pipeline.MainRenderNode.createFullScreenQuad()"""
        return 'graphics.Mesh'._wrap(super(MainRenderNode, self).createFullScreenQuad())

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float._wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str._wrap(super(RenderNode, self).dump())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def blur(self, arg0: float):
        """public void dev.ultreon.quantum.client.render.pipeline.MainRenderNode.blur(float)"""
        super(_MainRenderNode, self).blur(_float.valueOf(arg0))

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.requiresModel()"""
        return bool._wrap(super(RenderNode, self).requiresModel())

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'._wrap(super(RenderNode, self).getFrameBuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.MainRenderNode
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.render.pipeline.MainRenderNode as _MainRenderNode
_MainRenderNode = _MainRenderNode
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pyquantum.client import input
except ImportError:
    input = _import_once("pyquantum.client.input")

import java.io.PrintStream as PrintStream
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as _RenderPipeline_RenderNode
_RenderNode = _RenderPipeline_RenderNode.RenderNode
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

import com.badlogic.gdx.graphics.Mesh as _Mesh
_Mesh = _Mesh
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MainRenderNode():
    """dev.ultreon.quantum.client.render.pipeline.MainRenderNode"""
 
    @staticmethod
    def _wrap(java_value: _MainRenderNode) -> 'MainRenderNode':
        return MainRenderNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MainRenderNode):
        """
        Dynamic initializer for MainRenderNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MainRenderNode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MainRenderNode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.MainRenderNode.dumpInfo(java.io.PrintStream)"""
        super(_MainRenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.MainRenderNode.resize(int,int)"""
        super(_MainRenderNode, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.MainRenderNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'._wrap(super(_MainRenderNode, self).render(arg0, arg1, arg2, arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.MainRenderNode()"""
        val = _MainRenderNode()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dispose()"""
        super(RenderNode, self).dispose()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.MainRenderNode()"""
        val = _MainRenderNode()
        self.__wrapper = val

    @overload
    def createFullScreenQuad(self) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.pipeline.MainRenderNode.createFullScreenQuad()"""
        return 'graphics.Mesh'._wrap(super(MainRenderNode, self).createFullScreenQuad())

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float._wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str._wrap(super(RenderNode, self).dump())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def blur(self, arg0: float):
        """public void dev.ultreon.quantum.client.render.pipeline.MainRenderNode.blur(float)"""
        super(_MainRenderNode, self).blur(_float.valueOf(arg0))

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.requiresModel()"""
        return bool._wrap(super(RenderNode, self).requiresModel())

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'._wrap(super(RenderNode, self).getFrameBuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.MainRenderNode 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
try:
    from pyquantum.client import input
except ImportError:
    input = _import_once("pyquantum.client.input")

import java.io.PrintStream as PrintStream
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as _RenderPipeline_RenderNode
_RenderNode = _RenderPipeline_RenderNode.RenderNode
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RenderNode():
    """dev.ultreon.quantum.client.render.pipeline.RenderPipeline.RenderNode"""
 
    @staticmethod
    def _wrap(java_value: _RenderNode) -> 'RenderNode':
        return RenderNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderNode):
        """
        Dynamic initializer for RenderNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderNode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderNode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode()"""
        val = _RenderNode()
        self.__wrapper = val

    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str._wrap(super(RenderNode, self).dump())

    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float._wrap(super(RenderNode, self).getTime())

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
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dumpInfo(java.io.PrintStream)"""
        super(_RenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'._wrap(super(RenderNode, self).getFrameBuffer())

    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @abstractmethod
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array'):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        pass

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
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dispose()"""
        super(RenderNode, self).dispose()

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
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.requiresModel()"""
        return bool._wrap(super(RenderNode, self).requiresModel())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode()"""
        val = _RenderNode()
        self.__wrapper = val

    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(_RenderNode, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.WorldDepthNode
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import dev.ultreon.quantum.client.render.pipeline.WorldDepthNode as _WorldDepthNode
_WorldDepthNode = _WorldDepthNode
import dev.ultreon.quantum.client.render.pipeline.WorldRenderNode as _WorldRenderNode
_WorldRenderNode = _WorldRenderNode
try:
    from pyquantum.client import input
except ImportError:
    input = _import_once("pyquantum.client.input")

import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as _RenderPipeline_RenderNode
_RenderNode = _RenderPipeline_RenderNode.RenderNode
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldDepthNode():
    """dev.ultreon.quantum.client.render.pipeline.WorldDepthNode"""
 
    @staticmethod
    def _wrap(java_value: _WorldDepthNode) -> 'WorldDepthNode':
        return WorldDepthNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldDepthNode):
        """
        Dynamic initializer for WorldDepthNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldDepthNode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldDepthNode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.WorldDepthNode()"""
        val = _WorldDepthNode()
        self.__wrapper = val

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.requiresModel()"""
        return bool._wrap(super(WorldRenderNode, self).requiresModel())

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
        """public dev.ultreon.quantum.client.render.pipeline.WorldDepthNode()"""
        val = _WorldDepthNode()
        self.__wrapper = val

    @override
    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(_WorldRenderNode, self).setTexture(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dispose()"""
        super(RenderNode, self).dispose()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def renderWorld(self, arg0: 'ModelBatch'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.renderWorld(com.badlogic.gdx.graphics.g3d.ModelBatch)"""
        super(_WorldRenderNode, self).renderWorld(arg0)

    @overload
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.WorldDepthNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'._wrap(super(_WorldDepthNode, self).render(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float._wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str._wrap(super(RenderNode, self).dump())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.dumpInfo(java.io.PrintStream)"""
        super(_WorldRenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(_RenderNode, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'._wrap(super(RenderNode, self).getFrameBuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode$RenderableFlushablePool
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.utils.FlushablePool as _FlushablePool
_FlushablePool = _FlushablePool
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
import com.badlogic.gdx.graphics.g3d.Renderable as _Renderable
_Renderable = _Renderable
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as _RenderPipeline_RenderNode_RenderableFlushablePool
_RenderableFlushablePool = _RenderPipeline_RenderNode_RenderableFlushablePool.RenderNode.RenderableFlushablePool
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RenderableFlushablePool():
    """dev.ultreon.quantum.client.render.pipeline.RenderPipeline.RenderNode.RenderableFlushablePool"""
 
    @staticmethod
    def _wrap(java_value: _RenderableFlushablePool) -> 'RenderableFlushablePool':
        return RenderableFlushablePool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderableFlushablePool):
        """
        Dynamic initializer for RenderableFlushablePool.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderableFlushablePool__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderableFlushablePool__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode$RenderableFlushablePool()"""
        val = _RenderableFlushablePool()
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.Pool.clear()"""
        super(utils.Pool, self).clear()

    @override
    @overload
    def getFree(self) -> int:
        """public int com.badlogic.gdx.utils.Pool.getFree()"""
        return int._wrap(super(utils.Pool, self).getFree())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def fill(self, arg0: int):
        """public void com.badlogic.gdx.utils.Pool.fill(int)"""
        super(_utils.Pool, self).fill(_int.valueOf(arg0))

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
    def free(self, arg0: object):
        """public void com.badlogic.gdx.utils.FlushablePool.free(T)"""
        super(_utils.FlushablePool, self).free(arg0)

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
    def obtain(self) -> 'g3d.Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode$RenderableFlushablePool.obtain()"""
        return 'g3d.Renderable'._wrap(super(RenderableFlushablePool, self).obtain())

    @overload
    def getObtained(self) -> int:
        """public int dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode$RenderableFlushablePool.getObtained()"""
        return int._wrap(super(RenderableFlushablePool, self).getObtained())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode$RenderableFlushablePool()"""
        val = _RenderableFlushablePool()
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
    def freeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.FlushablePool.freeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(_utils.FlushablePool, self).freeAll(arg0)

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.utils.FlushablePool.flush()"""
        super(utils.FlushablePool, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.RenderPipeline
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as _RenderPipeline
_RenderPipeline = _RenderPipeline
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pyquantum.client import input
except ImportError:
    input = _import_once("pyquantum.client.input")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RenderPipeline():
    """dev.ultreon.quantum.client.render.pipeline.RenderPipeline"""
 
    @staticmethod
    def _wrap(java_value: _RenderPipeline) -> 'RenderPipeline':
        return RenderPipeline(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderPipeline):
        """
        Dynamic initializer for RenderPipeline.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderPipeline__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderPipeline__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline.resize(int,int)"""
        super(_RenderPipeline, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline.dispose()"""
        super(RenderPipeline, self).dispose()

    @overload
    def render(self, arg0: 'ModelBatch', arg1: float):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline.render(com.badlogic.gdx.graphics.g3d.ModelBatch,float)"""
        super(_RenderPipeline, self).render(arg0, _float.valueOf(arg1))

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
    def node(self, arg0: 'RenderNode') -> 'RenderPipeline':
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline dev.ultreon.quantum.client.render.pipeline.RenderPipeline.node(dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode)"""
        return 'RenderPipeline'._wrap(super(_RenderPipeline, self).node(arg0))

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
    def __init__(self, arg0: 'RenderNode', arg1: 'GameCamera'):
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline(dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode,dev.ultreon.quantum.client.input.GameCamera)"""
        val = _RenderPipeline(arg0, arg1)
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
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.CollectNode
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
try:
    from pyquantum.client import input
except ImportError:
    input = _import_once("pyquantum.client.input")

import java.lang.Integer as _int
import java.io.PrintStream as PrintStream
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as _RenderPipeline_RenderNode
_RenderNode = _RenderPipeline_RenderNode.RenderNode
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

import dev.ultreon.quantum.client.render.pipeline.CollectNode as _CollectNode
_CollectNode = _CollectNode
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CollectNode():
    """dev.ultreon.quantum.client.render.pipeline.CollectNode"""
 
    @staticmethod
    def _wrap(java_value: _CollectNode) -> 'CollectNode':
        return CollectNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CollectNode):
        """
        Dynamic initializer for CollectNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CollectNode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CollectNode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.CollectNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'._wrap(super(_CollectNode, self).render(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dumpInfo(java.io.PrintStream)"""
        super(_RenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.CollectNode()"""
        val = _CollectNode()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.CollectNode()"""
        val = _CollectNode()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dispose()"""
        super(RenderNode, self).dispose()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float._wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str._wrap(super(RenderNode, self).dump())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(_RenderNode, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.requiresModel()"""
        return bool._wrap(super(RenderNode, self).requiresModel())

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'._wrap(super(RenderNode, self).getFrameBuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.WorldRenderNode
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.render.pipeline.WorldRenderNode as _WorldRenderNode
_WorldRenderNode = _WorldRenderNode
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
try:
    from pyquantum.client import input
except ImportError:
    input = _import_once("pyquantum.client.input")

import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as _RenderPipeline_RenderNode
_RenderNode = _RenderPipeline_RenderNode.RenderNode
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldRenderNode():
    """dev.ultreon.quantum.client.render.pipeline.WorldRenderNode"""
 
    @staticmethod
    def _wrap(java_value: _WorldRenderNode) -> 'WorldRenderNode':
        return WorldRenderNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldRenderNode):
        """
        Dynamic initializer for WorldRenderNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldRenderNode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldRenderNode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.WorldRenderNode()"""
        val = _WorldRenderNode()
        self.__wrapper = val

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.requiresModel()"""
        return bool._wrap(super(WorldRenderNode, self).requiresModel())

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
    def setTexture(self, arg0: 'Texture'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(_WorldRenderNode, self).setTexture(arg0)

    @abstractmethod
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array'):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dispose()"""
        super(RenderNode, self).dispose()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float._wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str._wrap(super(RenderNode, self).dump())

    @overload
    def renderWorld(self, arg0: 'ModelBatch'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.renderWorld(com.badlogic.gdx.graphics.g3d.ModelBatch)"""
        super(_WorldRenderNode, self).renderWorld(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.WorldRenderNode()"""
        val = _WorldRenderNode()
        self.__wrapper = val

    @override
    @overload
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.dumpInfo(java.io.PrintStream)"""
        super(_WorldRenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(_RenderNode, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'._wrap(super(RenderNode, self).getFrameBuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.PostEffectsNode
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
try:
    from pyquantum.client import input
except ImportError:
    input = _import_once("pyquantum.client.input")

import java.lang.Integer as _int
import java.io.PrintStream as PrintStream
import dev.ultreon.quantum.client.render.pipeline.PostEffectsNode as _PostEffectsNode
_PostEffectsNode = _PostEffectsNode
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as _RenderPipeline_RenderNode
_RenderNode = _RenderPipeline_RenderNode.RenderNode
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PostEffectsNode():
    """dev.ultreon.quantum.client.render.pipeline.PostEffectsNode"""
 
    @staticmethod
    def _wrap(java_value: _PostEffectsNode) -> 'PostEffectsNode':
        return PostEffectsNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PostEffectsNode):
        """
        Dynamic initializer for PostEffectsNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PostEffectsNode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PostEffectsNode__wrapper":
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
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dumpInfo(java.io.PrintStream)"""
        super(_RenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.PostEffectsNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'._wrap(super(_PostEffectsNode, self).render(arg0, arg1, arg2, arg3))

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
        """public dev.ultreon.quantum.client.render.pipeline.PostEffectsNode()"""
        val = _PostEffectsNode()
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dispose()"""
        super(RenderNode, self).dispose()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float._wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.PostEffectsNode()"""
        val = _PostEffectsNode()
        self.__wrapper = val

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str._wrap(super(RenderNode, self).dump())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(_RenderNode, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.requiresModel()"""
        return bool._wrap(super(RenderNode, self).requiresModel())

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'._wrap(super(RenderNode, self).getFrameBuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.BackgroundNode
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
try:
    from pyquantum.client import input
except ImportError:
    input = _import_once("pyquantum.client.input")

import java.lang.Integer as _int
import java.io.PrintStream as PrintStream
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as _RenderPipeline_RenderNode
_RenderNode = _RenderPipeline_RenderNode.RenderNode
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

from builtins import bool
import dev.ultreon.quantum.client.render.pipeline.BackgroundNode as _BackgroundNode
_BackgroundNode = _BackgroundNode
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BackgroundNode():
    """dev.ultreon.quantum.client.render.pipeline.BackgroundNode"""
 
    @staticmethod
    def _wrap(java_value: _BackgroundNode) -> 'BackgroundNode':
        return BackgroundNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BackgroundNode):
        """
        Dynamic initializer for BackgroundNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BackgroundNode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BackgroundNode__wrapper":
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
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dumpInfo(java.io.PrintStream)"""
        super(_RenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.BackgroundNode()"""
        val = _BackgroundNode()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def renderWorld(self, arg0: 'ModelBatch'):
        """public void dev.ultreon.quantum.client.render.pipeline.BackgroundNode.renderWorld(com.badlogic.gdx.graphics.g3d.ModelBatch)"""
        super(_BackgroundNode, self).renderWorld(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dispose()"""
        super(RenderNode, self).dispose()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float._wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.BackgroundNode()"""
        val = _BackgroundNode()
        self.__wrapper = val

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.BackgroundNode.requiresModel()"""
        return bool._wrap(super(BackgroundNode, self).requiresModel())

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str._wrap(super(RenderNode, self).dump())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.BackgroundNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'._wrap(super(_BackgroundNode, self).render(arg0, arg1, arg2, arg3))

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(_RenderNode, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'._wrap(super(RenderNode, self).getFrameBuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.WorldDiffuseNode
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import dev.ultreon.quantum.client.render.pipeline.WorldDiffuseNode as _WorldDiffuseNode
_WorldDiffuseNode = _WorldDiffuseNode
import dev.ultreon.quantum.client.render.pipeline.WorldRenderNode as _WorldRenderNode
_WorldRenderNode = _WorldRenderNode
try:
    from pyquantum.client import input
except ImportError:
    input = _import_once("pyquantum.client.input")

import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as _RenderPipeline_RenderNode
_RenderNode = _RenderPipeline_RenderNode.RenderNode
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldDiffuseNode():
    """dev.ultreon.quantum.client.render.pipeline.WorldDiffuseNode"""
 
    @staticmethod
    def _wrap(java_value: _WorldDiffuseNode) -> 'WorldDiffuseNode':
        return WorldDiffuseNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldDiffuseNode):
        """
        Dynamic initializer for WorldDiffuseNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldDiffuseNode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldDiffuseNode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.WorldDiffuseNode()"""
        val = _WorldDiffuseNode()
        self.__wrapper = val

    @overload
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.WorldDiffuseNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'._wrap(super(_WorldDiffuseNode, self).render(arg0, arg1, arg2, arg3))

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.requiresModel()"""
        return bool._wrap(super(WorldRenderNode, self).requiresModel())

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
    def setTexture(self, arg0: 'Texture'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(_WorldRenderNode, self).setTexture(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dispose()"""
        super(RenderNode, self).dispose()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def renderWorld(self, arg0: 'ModelBatch'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.renderWorld(com.badlogic.gdx.graphics.g3d.ModelBatch)"""
        super(_WorldRenderNode, self).renderWorld(arg0)

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float._wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str._wrap(super(RenderNode, self).dump())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.WorldDiffuseNode()"""
        val = _WorldDiffuseNode()
        self.__wrapper = val

    @override
    @overload
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.dumpInfo(java.io.PrintStream)"""
        super(_WorldRenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(_RenderNode, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'._wrap(super(RenderNode, self).getFrameBuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())