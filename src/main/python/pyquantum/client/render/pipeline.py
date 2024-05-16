from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import dev.ultreon.quantum.client.render.pipeline.MainRenderNode as __MainRenderNode
__MainRenderNode = __MainRenderNode
from pyquantum_helper import override
import com.badlogic.gdx.graphics.Mesh as __Mesh
__Mesh = __Mesh
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as __RenderPipeline_RenderNode
__RenderNode = __RenderPipeline_RenderNode.RenderNode
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.client import input
except ImportError:
    input = __import_once__("pyquantum.client.input")

import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
from builtins import bool
from builtins import int
 
class MainRenderNode(__RenderNode, RenderNode):
    """dev.ultreon.quantum.client.render.pipeline.MainRenderNode"""
 
    @staticmethod
    def __wrap(java_value: __MainRenderNode) -> 'MainRenderNode':
        return MainRenderNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MainRenderNode):
        """
        Dynamic initializer for MainRenderNode.
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
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str.__wrap(super(RenderNode, self).dump())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.MainRenderNode.resize(int,int)"""
        super(__MainRenderNode, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def blur(self, arg0: float):
        """public void dev.ultreon.quantum.client.render.pipeline.MainRenderNode.blur(float)"""
        super(__MainRenderNode, self).blur(__float.valueOf(arg0))

    @overload
    def createFullScreenQuad(self) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.pipeline.MainRenderNode.createFullScreenQuad()"""
        return 'graphics.Mesh'.__wrap(super(MainRenderNode, self).createFullScreenQuad())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.MainRenderNode()"""
        val = __MainRenderNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float.__wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.requiresModel()"""
        return bool.__wrap(super(RenderNode, self).requiresModel())

    @override
    @overload
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.MainRenderNode.dumpInfo(java.io.PrintStream)"""
        super(__MainRenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

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
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.MainRenderNode()"""
        val = __MainRenderNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.MainRenderNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'.__wrap(super(__MainRenderNode, self).render(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'.__wrap(super(RenderNode, self).getFrameBuffer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.MainRenderNode
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import dev.ultreon.quantum.client.render.pipeline.MainRenderNode as __MainRenderNode
__MainRenderNode = __MainRenderNode
from pyquantum_helper import override
import com.badlogic.gdx.graphics.Mesh as __Mesh
__Mesh = __Mesh
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as __RenderPipeline_RenderNode
__RenderNode = __RenderPipeline_RenderNode.RenderNode
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.client import input
except ImportError:
    input = __import_once__("pyquantum.client.input")

import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
from builtins import bool
from builtins import int
 
class MainRenderNode(__RenderNode, RenderNode):
    """dev.ultreon.quantum.client.render.pipeline.MainRenderNode"""
 
    @staticmethod
    def __wrap(java_value: __MainRenderNode) -> 'MainRenderNode':
        return MainRenderNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MainRenderNode):
        """
        Dynamic initializer for MainRenderNode.
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
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str.__wrap(super(RenderNode, self).dump())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.MainRenderNode.resize(int,int)"""
        super(__MainRenderNode, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def blur(self, arg0: float):
        """public void dev.ultreon.quantum.client.render.pipeline.MainRenderNode.blur(float)"""
        super(__MainRenderNode, self).blur(__float.valueOf(arg0))

    @overload
    def createFullScreenQuad(self) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh dev.ultreon.quantum.client.render.pipeline.MainRenderNode.createFullScreenQuad()"""
        return 'graphics.Mesh'.__wrap(super(MainRenderNode, self).createFullScreenQuad())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.MainRenderNode()"""
        val = __MainRenderNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float.__wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.requiresModel()"""
        return bool.__wrap(super(RenderNode, self).requiresModel())

    @override
    @overload
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.MainRenderNode.dumpInfo(java.io.PrintStream)"""
        super(__MainRenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

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
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.MainRenderNode()"""
        val = __MainRenderNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.MainRenderNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'.__wrap(super(__MainRenderNode, self).render(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'.__wrap(super(RenderNode, self).getFrameBuffer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.MainRenderNode 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as __RenderPipeline_RenderNode
__RenderNode = __RenderPipeline_RenderNode.RenderNode
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
from builtins import float
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.client import input
except ImportError:
    input = __import_once__("pyquantum.client.input")

import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
from builtins import bool
from builtins import int
 
class RenderNode(ABC):
    """dev.ultreon.quantum.client.render.pipeline.RenderPipeline.RenderNode"""
 
    @staticmethod
    def __wrap(java_value: __RenderNode) -> 'RenderNode':
        return RenderNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderNode):
        """
        Dynamic initializer for RenderNode.
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
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dumpInfo(java.io.PrintStream)"""
        super(__RenderNode, self).dumpInfo(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode()"""
        val = __RenderNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(__RenderNode, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'.__wrap(super(RenderNode, self).getFrameBuffer())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float.__wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode()"""
        val = __RenderNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @abstractmethod
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array'):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        pass

    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.requiresModel()"""
        return bool.__wrap(super(RenderNode, self).requiresModel())

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
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dispose()"""
        super(RenderNode, self).dispose()

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
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str.__wrap(super(RenderNode, self).dump())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.WorldDepthNode
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as __RenderPipeline_RenderNode
__RenderNode = __RenderPipeline_RenderNode.RenderNode
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.client import input
except ImportError:
    input = __import_once__("pyquantum.client.input")

import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.render.pipeline.WorldRenderNode as __WorldRenderNode
__WorldRenderNode = __WorldRenderNode
import java.lang.Integer as __int
import dev.ultreon.quantum.client.render.pipeline.WorldDepthNode as __WorldDepthNode
__WorldDepthNode = __WorldDepthNode
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
from builtins import int
 
class WorldDepthNode(__WorldRenderNode, WorldRenderNode):
    """dev.ultreon.quantum.client.render.pipeline.WorldDepthNode"""
 
    @staticmethod
    def __wrap(java_value: __WorldDepthNode) -> 'WorldDepthNode':
        return WorldDepthNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldDepthNode):
        """
        Dynamic initializer for WorldDepthNode.
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
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.WorldDepthNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'.__wrap(super(__WorldDepthNode, self).render(arg0, arg1, arg2, arg3))

    @override
    @overload
    def renderWorld(self, arg0: 'ModelBatch'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.renderWorld(com.badlogic.gdx.graphics.g3d.ModelBatch)"""
        super(__WorldRenderNode, self).renderWorld(arg0)

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str.__wrap(super(RenderNode, self).dump())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.WorldDepthNode()"""
        val = __WorldDepthNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(__WorldRenderNode, self).setTexture(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float.__wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

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
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.dumpInfo(java.io.PrintStream)"""
        super(__WorldRenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.WorldDepthNode()"""
        val = __WorldDepthNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.requiresModel()"""
        return bool.__wrap(super(WorldRenderNode, self).requiresModel())

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'.__wrap(super(RenderNode, self).getFrameBuffer())

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(__RenderNode, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode$RenderableFlushablePool
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as __RenderPipeline_RenderNode_RenderableFlushablePool
__RenderableFlushablePool = __RenderPipeline_RenderNode_RenderableFlushablePool.RenderNode.RenderableFlushablePool
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.utils.FlushablePool as __FlushablePool
__FlushablePool = __FlushablePool
import com.badlogic.gdx.graphics.g3d.Renderable as __Renderable
__Renderable = __Renderable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RenderableFlushablePool(pygdx.__FlushablePool, utils.FlushablePool):
    """dev.ultreon.quantum.client.render.pipeline.RenderPipeline.RenderNode.RenderableFlushablePool"""
 
    @staticmethod
    def __wrap(java_value: __RenderableFlushablePool) -> 'RenderableFlushablePool':
        return RenderableFlushablePool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderableFlushablePool):
        """
        Dynamic initializer for RenderableFlushablePool.
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
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.Pool.clear()"""
        super(utils.Pool, self).clear()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode$RenderableFlushablePool()"""
        val = __RenderableFlushablePool()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def fill(self, arg0: int):
        """public void com.badlogic.gdx.utils.Pool.fill(int)"""
        super(__utils.Pool, self).fill(__int.valueOf(arg0))

    @override
    @overload
    def getFree(self) -> int:
        """public int com.badlogic.gdx.utils.Pool.getFree()"""
        return int.__wrap(super(utils.Pool, self).getFree())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def freeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.FlushablePool.freeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(__utils.FlushablePool, self).freeAll(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def free(self, arg0: object):
        """public void com.badlogic.gdx.utils.FlushablePool.free(T)"""
        super(__utils.FlushablePool, self).free(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def obtain(self) -> 'g3d.Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode$RenderableFlushablePool.obtain()"""
        return 'g3d.Renderable'.__wrap(super(RenderableFlushablePool, self).obtain())

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
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode$RenderableFlushablePool()"""
        val = __RenderableFlushablePool()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getObtained(self) -> int:
        """public int dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode$RenderableFlushablePool.getObtained()"""
        return int.__wrap(super(RenderableFlushablePool, self).getObtained())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.utils.FlushablePool.flush()"""
        super(utils.FlushablePool, self).flush() 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.RenderPipeline
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as __RenderPipeline
__RenderPipeline = __RenderPipeline
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.client import input
except ImportError:
    input = __import_once__("pyquantum.client.input")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RenderPipeline(pygdx.__Disposable, utils.Disposable):
    """dev.ultreon.quantum.client.render.pipeline.RenderPipeline"""
 
    @staticmethod
    def __wrap(java_value: __RenderPipeline) -> 'RenderPipeline':
        return RenderPipeline(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderPipeline):
        """
        Dynamic initializer for RenderPipeline.
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
    def dispose(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline.dispose()"""
        super(RenderPipeline, self).dispose()

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
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline.resize(int,int)"""
        super(__RenderPipeline, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'RenderNode', arg1: 'GameCamera'):
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline(dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode,dev.ultreon.quantum.client.input.GameCamera)"""
        val = __RenderPipeline(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def render(self, arg0: 'ModelBatch', arg1: float):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline.render(com.badlogic.gdx.graphics.g3d.ModelBatch,float)"""
        super(__RenderPipeline, self).render(arg0, __float.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def node(self, arg0: 'RenderNode') -> 'RenderPipeline':
        """public dev.ultreon.quantum.client.render.pipeline.RenderPipeline dev.ultreon.quantum.client.render.pipeline.RenderPipeline.node(dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode)"""
        return 'RenderPipeline'.__wrap(super(__RenderPipeline, self).node(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.CollectNode
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as __RenderPipeline_RenderNode
__RenderNode = __RenderPipeline_RenderNode.RenderNode
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
from builtins import float
import dev.ultreon.quantum.client.render.pipeline.CollectNode as __CollectNode
__CollectNode = __CollectNode
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.client import input
except ImportError:
    input = __import_once__("pyquantum.client.input")

import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
from builtins import bool
from builtins import int
 
class CollectNode(__RenderNode, RenderNode):
    """dev.ultreon.quantum.client.render.pipeline.CollectNode"""
 
    @staticmethod
    def __wrap(java_value: __CollectNode) -> 'CollectNode':
        return CollectNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CollectNode):
        """
        Dynamic initializer for CollectNode.
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
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str.__wrap(super(RenderNode, self).dump())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.CollectNode()"""
        val = __CollectNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.CollectNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'.__wrap(super(__CollectNode, self).render(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float.__wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.requiresModel()"""
        return bool.__wrap(super(RenderNode, self).requiresModel())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'.__wrap(super(RenderNode, self).getFrameBuffer())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.CollectNode()"""
        val = __CollectNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(__RenderNode, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dumpInfo(java.io.PrintStream)"""
        super(__RenderNode, self).dumpInfo(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.WorldRenderNode
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as __RenderPipeline_RenderNode
__RenderNode = __RenderPipeline_RenderNode.RenderNode
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
from builtins import float
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
try:
    from pyquantum.client import input
except ImportError:
    input = __import_once__("pyquantum.client.input")

import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.render.pipeline.WorldRenderNode as __WorldRenderNode
__WorldRenderNode = __WorldRenderNode
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
from builtins import int
 
class WorldRenderNode(ABC, __RenderNode, RenderNode):
    """dev.ultreon.quantum.client.render.pipeline.WorldRenderNode"""
 
    @staticmethod
    def __wrap(java_value: __WorldRenderNode) -> 'WorldRenderNode':
        return WorldRenderNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldRenderNode):
        """
        Dynamic initializer for WorldRenderNode.
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
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str.__wrap(super(RenderNode, self).dump())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def renderWorld(self, arg0: 'ModelBatch'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.renderWorld(com.badlogic.gdx.graphics.g3d.ModelBatch)"""
        super(__WorldRenderNode, self).renderWorld(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.WorldRenderNode()"""
        val = __WorldRenderNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float.__wrap(super(RenderNode, self).getTime())

    @abstractmethod
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array'):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(__WorldRenderNode, self).setTexture(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.WorldRenderNode()"""
        val = __WorldRenderNode()
        self.__dict__ = val.__dict__
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
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.dumpInfo(java.io.PrintStream)"""
        super(__WorldRenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.requiresModel()"""
        return bool.__wrap(super(WorldRenderNode, self).requiresModel())

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'.__wrap(super(RenderNode, self).getFrameBuffer())

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(__RenderNode, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.PostEffectsNode
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as __RenderPipeline_RenderNode
__RenderNode = __RenderPipeline_RenderNode.RenderNode
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
from builtins import float
import java.lang.Long as __long
import dev.ultreon.quantum.client.render.pipeline.PostEffectsNode as __PostEffectsNode
__PostEffectsNode = __PostEffectsNode
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.client import input
except ImportError:
    input = __import_once__("pyquantum.client.input")

import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
from builtins import bool
from builtins import int
 
class PostEffectsNode(__RenderNode, RenderNode):
    """dev.ultreon.quantum.client.render.pipeline.PostEffectsNode"""
 
    @staticmethod
    def __wrap(java_value: __PostEffectsNode) -> 'PostEffectsNode':
        return PostEffectsNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PostEffectsNode):
        """
        Dynamic initializer for PostEffectsNode.
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
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.PostEffectsNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'.__wrap(super(__PostEffectsNode, self).render(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.PostEffectsNode()"""
        val = __PostEffectsNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str.__wrap(super(RenderNode, self).dump())

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
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float.__wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.requiresModel()"""
        return bool.__wrap(super(RenderNode, self).requiresModel())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'.__wrap(super(RenderNode, self).getFrameBuffer())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.PostEffectsNode()"""
        val = __PostEffectsNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(__RenderNode, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dumpInfo(java.io.PrintStream)"""
        super(__RenderNode, self).dumpInfo(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.BackgroundNode
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as __RenderPipeline_RenderNode
__RenderNode = __RenderPipeline_RenderNode.RenderNode
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.client import input
except ImportError:
    input = __import_once__("pyquantum.client.input")

import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.render.pipeline.BackgroundNode as __BackgroundNode
__BackgroundNode = __BackgroundNode
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
from builtins import int
 
class BackgroundNode(__RenderNode, RenderNode):
    """dev.ultreon.quantum.client.render.pipeline.BackgroundNode"""
 
    @staticmethod
    def __wrap(java_value: __BackgroundNode) -> 'BackgroundNode':
        return BackgroundNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BackgroundNode):
        """
        Dynamic initializer for BackgroundNode.
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
        """public dev.ultreon.quantum.client.render.pipeline.BackgroundNode()"""
        val = __BackgroundNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str.__wrap(super(RenderNode, self).dump())

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.BackgroundNode()"""
        val = __BackgroundNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float.__wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def renderWorld(self, arg0: 'ModelBatch'):
        """public void dev.ultreon.quantum.client.render.pipeline.BackgroundNode.renderWorld(com.badlogic.gdx.graphics.g3d.ModelBatch)"""
        super(__BackgroundNode, self).renderWorld(arg0)

    @overload
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.BackgroundNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'.__wrap(super(__BackgroundNode, self).render(arg0, arg1, arg2, arg3))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'.__wrap(super(RenderNode, self).getFrameBuffer())

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.BackgroundNode.requiresModel()"""
        return bool.__wrap(super(BackgroundNode, self).requiresModel())

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(__RenderNode, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dumpInfo(java.io.PrintStream)"""
        super(__RenderNode, self).dumpInfo(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.render.pipeline.WorldDiffuseNode
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.render.pipeline.WorldDiffuseNode as __WorldDiffuseNode
__WorldDiffuseNode = __WorldDiffuseNode
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import dev.ultreon.quantum.client.render.pipeline.RenderPipeline as __RenderPipeline_RenderNode
__RenderNode = __RenderPipeline_RenderNode.RenderNode
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum.client import input
except ImportError:
    input = __import_once__("pyquantum.client.input")

import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.render.pipeline.WorldRenderNode as __WorldRenderNode
__WorldRenderNode = __WorldRenderNode
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
from builtins import int
 
class WorldDiffuseNode(__WorldRenderNode, WorldRenderNode):
    """dev.ultreon.quantum.client.render.pipeline.WorldDiffuseNode"""
 
    @staticmethod
    def __wrap(java_value: __WorldDiffuseNode) -> 'WorldDiffuseNode':
        return WorldDiffuseNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldDiffuseNode):
        """
        Dynamic initializer for WorldDiffuseNode.
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
    def render(self, arg0: 'ObjectMap', arg1: 'ModelBatch', arg2: 'GameCamera', arg3: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable> dev.ultreon.quantum.client.render.pipeline.WorldDiffuseNode.render(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>,com.badlogic.gdx.graphics.g3d.ModelBatch,dev.ultreon.quantum.client.input.GameCamera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        return 'utils.Array'.__wrap(super(__WorldDiffuseNode, self).render(arg0, arg1, arg2, arg3))

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

    @override
    @overload
    def renderWorld(self, arg0: 'ModelBatch'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.renderWorld(com.badlogic.gdx.graphics.g3d.ModelBatch)"""
        super(__WorldRenderNode, self).renderWorld(arg0)

    @override
    @overload
    def dump(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.dump()"""
        return str.__wrap(super(RenderNode, self).dump())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.pipeline.WorldDiffuseNode()"""
        val = __WorldDiffuseNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(__WorldRenderNode, self).setTexture(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getTime(self) -> float:
        """public float dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getTime()"""
        return float.__wrap(super(RenderNode, self).getTime())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

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
    def dumpInfo(self, arg0: 'PrintStream'):
        """public void dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.dumpInfo(java.io.PrintStream)"""
        super(__WorldRenderNode, self).dumpInfo(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def requiresModel(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.pipeline.WorldRenderNode.requiresModel()"""
        return bool.__wrap(super(WorldRenderNode, self).requiresModel())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.pipeline.WorldDiffuseNode()"""
        val = __WorldDiffuseNode()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.getFrameBuffer()"""
        return 'glutils.FrameBuffer'.__wrap(super(RenderNode, self).getFrameBuffer())

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.resize(int,int)"""
        super(__RenderNode, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def flush(self):
        """public void dev.ultreon.quantum.client.render.pipeline.RenderPipeline$RenderNode.flush()"""
        super(RenderNode, self).flush()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))