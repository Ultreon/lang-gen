from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.model.Animation as _Animation
_Animation = _Animation
try:
    from pyquantum.client.model import blockbench
except ImportError:
    blockbench = _import_once("pyquantum.client.model.blockbench")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.String as _string
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator as _BBAnimator
_BBAnimator = _BBAnimator
import java.lang.Integer as _int
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = _import_once("pygdx.graphics.g3d.model")

import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator as _BBAnimator_Type
_Type = _BBAnimator_Type.Type
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class BBAnimator():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator"""
 
    @staticmethod
    def _wrap(java_value: _BBAnimator) -> 'BBAnimator':
        return BBAnimator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBAnimator):
        """
        Dynamic initializer for BBAnimator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBAnimator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBAnimator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.hashCode()"""
        return int._wrap(super(BBAnimator, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.equals(java.lang.Object)"""
        return bool._wrap(super(_BBAnimator, self).equals(arg0))

    @overload
    def build(self, arg0: 'Node', arg1: 'BBModelLoader', arg2: 'Animation', arg3: 'Map') -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.build(com.badlogic.gdx.graphics.g3d.model.Node,dev.ultreon.quantum.client.model.blockbench.BBModelLoader,com.badlogic.gdx.graphics.g3d.model.Animation,java.util.Map<com.badlogic.gdx.graphics.g3d.model.Node, com.badlogic.gdx.graphics.g3d.model.NodeAnimation>)"""
        return 'model.Animation'._wrap(super(_BBAnimator, self).build(arg0, arg1, arg2, arg3))

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
    def keyFrames(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame> dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.keyFrames()"""
        return 'List'._wrap(super(BBAnimator, self).keyFrames())

    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.type()"""
        return 'Type'._wrap(super(BBAnimator, self).type())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.toString()"""
        return str._wrap(super(BBAnimator, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.name()"""
        return str._wrap(super(BBAnimator, self).name())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: 'Type', arg2: 'List'):
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator(java.lang.String,dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type,java.util.List<dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame>)"""
        val = _BBAnimator(arg0, arg1, arg2)
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.model.Animation as _Animation
_Animation = _Animation
try:
    from pyquantum.client.model import blockbench
except ImportError:
    blockbench = _import_once("pyquantum.client.model.blockbench")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.String as _string
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator as _BBAnimator
_BBAnimator = _BBAnimator
import java.lang.Integer as _int
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = _import_once("pygdx.graphics.g3d.model")

import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator as _BBAnimator_Type
_Type = _BBAnimator_Type.Type
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class BBAnimator():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator"""
 
    @staticmethod
    def _wrap(java_value: _BBAnimator) -> 'BBAnimator':
        return BBAnimator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBAnimator):
        """
        Dynamic initializer for BBAnimator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBAnimator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBAnimator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.hashCode()"""
        return int._wrap(super(BBAnimator, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.equals(java.lang.Object)"""
        return bool._wrap(super(_BBAnimator, self).equals(arg0))

    @overload
    def build(self, arg0: 'Node', arg1: 'BBModelLoader', arg2: 'Animation', arg3: 'Map') -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.build(com.badlogic.gdx.graphics.g3d.model.Node,dev.ultreon.quantum.client.model.blockbench.BBModelLoader,com.badlogic.gdx.graphics.g3d.model.Animation,java.util.Map<com.badlogic.gdx.graphics.g3d.model.Node, com.badlogic.gdx.graphics.g3d.model.NodeAnimation>)"""
        return 'model.Animation'._wrap(super(_BBAnimator, self).build(arg0, arg1, arg2, arg3))

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
    def keyFrames(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame> dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.keyFrames()"""
        return 'List'._wrap(super(BBAnimator, self).keyFrames())

    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.type()"""
        return 'Type'._wrap(super(BBAnimator, self).type())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.toString()"""
        return str._wrap(super(BBAnimator, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.name()"""
        return str._wrap(super(BBAnimator, self).name())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: 'Type', arg2: 'List'):
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator(java.lang.String,dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type,java.util.List<dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame>)"""
        val = _BBAnimator(arg0, arg1, arg2)
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.model.Animation as _Animation
_Animation = _Animation
import java.util.Map as _Map
_Map = _Map
from builtins import float
try:
    from pyquantum.client.model import blockbench
except ImportError:
    blockbench = _import_once("pyquantum.client.model.blockbench")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation as _BBAnimation
_BBAnimation = _BBAnimation
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation as _BBAnimation_Loop
_Loop = _BBAnimation_Loop.Loop
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = _import_once("pygdx.graphics.g3d.model")

from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
 
class BBAnimation():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation"""
 
    @staticmethod
    def _wrap(java_value: _BBAnimation) -> 'BBAnimation':
        return BBAnimation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBAnimation):
        """
        Dynamic initializer for BBAnimation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBAnimation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBAnimation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.hashCode()"""
        return int._wrap(super(BBAnimation, self).hashCode())

    @overload
    def __init__(self, arg0: 'UUID', arg1: str, arg2: 'Loop', arg3: bool, arg4: float, arg5: int, arg6: bool, arg7: str, arg8: str, arg9: str, arg10: str, arg11: 'Map'):
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation(java.util.UUID,java.lang.String,dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop,boolean,float,int,boolean,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.util.Map<java.util.UUID, dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator>)"""
        val = _BBAnimation(arg0, arg1, arg2, _boolean.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _boolean.valueOf(arg6), arg7, arg8, arg9, arg10, arg11)
        self.__wrapper = val

    @overload
    def loopDelay(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.loopDelay()"""
        return str._wrap(super(BBAnimation, self).loopDelay())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.equals(java.lang.Object)"""
        return bool._wrap(super(_BBAnimation, self).equals(arg0))

    @overload
    def create(self, arg0: 'Map', arg1: 'BBModelLoader') -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.create(java.util.Map<java.util.UUID, com.badlogic.gdx.graphics.g3d.model.Node>,dev.ultreon.quantum.client.model.blockbench.BBModelLoader)"""
        return 'model.Animation'._wrap(super(_BBAnimation, self).create(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def snapping(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.snapping()"""
        return int._wrap(super(BBAnimation, self).snapping())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.toString()"""
        return str._wrap(super(BBAnimation, self).toString())

    @overload
    def startDelay(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.startDelay()"""
        return str._wrap(super(BBAnimation, self).startDelay())

    @overload
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.uuid()"""
        return 'UUID'._wrap(super(BBAnimation, self).uuid())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def override(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.override()"""
        return bool._wrap(super(BBAnimation, self).override())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def loop(self) -> 'Loop':
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.loop()"""
        return 'Loop'._wrap(super(BBAnimation, self).loop())

    @overload
    def animTimeUpdate(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.animTimeUpdate()"""
        return str._wrap(super(BBAnimation, self).animTimeUpdate())

    @overload
    def selected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.selected()"""
        return bool._wrap(super(BBAnimation, self).selected())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def blendWeight(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.blendWeight()"""
        return str._wrap(super(BBAnimation, self).blendWeight())

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.name()"""
        return str._wrap(super(BBAnimation, self).name())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def length(self) -> float:
        """public float dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.length()"""
        return float._wrap(super(BBAnimation, self).length())

    @overload
    def animators(self) -> 'Map':
        """public java.util.Map<java.util.UUID, dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator> dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.animators()"""
        return 'Map'._wrap(super(BBAnimation, self).animators()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel
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
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel as _BBAnimChannel
_BBAnimChannel = _BBAnimChannel
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BBAnimChannel():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel"""
 
    @staticmethod
    def _wrap(java_value: _BBAnimChannel) -> 'BBAnimChannel':
        return BBAnimChannel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBAnimChannel):
        """
        Dynamic initializer for BBAnimChannel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBAnimChannel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBAnimChannel__wrapper":
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

    @staticmethod
    @overload
    def values() -> List['BBAnimChannel']:
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel[] dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel.values()"""
        return List[BBAnimChannel]._wrap(_BBAnimChannel.values())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BBAnimChannel':
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel.valueOf(java.lang.String)"""
        return BBAnimChannel._wrap(_BBAnimChannel.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


BBAnimChannel.POSITION = BBAnimChannel._wrap(_POSITION.POSITION)

BBAnimChannel.SCALE = BBAnimChannel._wrap(_SCALE.SCALE)

BBAnimChannel.ROTATION = BBAnimChannel._wrap(_ROTATION.ROTATION) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame as _BBAnimKeyFrame
_BBAnimKeyFrame = _BBAnimKeyFrame
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum.client.model import blockbench
except ImportError:
    blockbench = _import_once("pyquantum.client.model.blockbench")

import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.blockbench.BBColor as _BBColor
_BBColor = _BBColor
import java.util.List as _List
_List = _List
import java.lang.Float as _float
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation as _BBAnimInterpolation
_BBAnimInterpolation = _BBAnimInterpolation
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel as _BBAnimChannel
_BBAnimChannel = _BBAnimChannel
import java.lang.Long as _long
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class BBAnimKeyFrame():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame"""
 
    @staticmethod
    def _wrap(java_value: _BBAnimKeyFrame) -> 'BBAnimKeyFrame':
        return BBAnimKeyFrame(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBAnimKeyFrame):
        """
        Dynamic initializer for BBAnimKeyFrame.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBAnimKeyFrame__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBAnimKeyFrame__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.equals(java.lang.Object)"""
        return bool._wrap(super(_BBAnimKeyFrame, self).equals(arg0))

    @overload
    def bezierRightValue(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.bezierRightValue()"""
        return 'math.Vector3'._wrap(super(BBAnimKeyFrame, self).bezierRightValue())

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
    def interpolation(self) -> 'BBAnimInterpolation':
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.interpolation()"""
        return 'BBAnimInterpolation'._wrap(super(BBAnimKeyFrame, self).interpolation())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def time(self) -> float:
        """public float dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.time()"""
        return float._wrap(super(BBAnimKeyFrame, self).time())

    @overload
    def bezierLinked(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.bezierLinked()"""
        return bool._wrap(super(BBAnimKeyFrame, self).bezierLinked())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def dataPoints(self) -> 'List':
        """public java.util.List<com.badlogic.gdx.math.Vector3> dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.dataPoints()"""
        return 'List'._wrap(super(BBAnimKeyFrame, self).dataPoints())

    @overload
    def bezierLeftTime(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.bezierLeftTime()"""
        return 'math.Vector3'._wrap(super(BBAnimKeyFrame, self).bezierLeftTime())

    @overload
    def bezierRightTime(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.bezierRightTime()"""
        return 'math.Vector3'._wrap(super(BBAnimKeyFrame, self).bezierRightTime())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.hashCode()"""
        return int._wrap(super(BBAnimKeyFrame, self).hashCode())

    @overload
    def bezierLeftValue(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.bezierLeftValue()"""
        return 'math.Vector3'._wrap(super(BBAnimKeyFrame, self).bezierLeftValue())

    @overload
    def color(self) -> 'blockbench.BBColor':
        """public dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.color()"""
        return 'blockbench.BBColor'._wrap(super(BBAnimKeyFrame, self).color())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'BBAnimChannel', arg1: 'List', arg2: 'UUID', arg3: float, arg4: 'BBColor', arg5: 'BBAnimInterpolation', arg6: bool, arg7: 'Vector3', arg8: 'Vector3', arg9: 'Vector3', arg10: 'Vector3'):
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame(dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel,java.util.List<com.badlogic.gdx.math.Vector3>,java.util.UUID,float,dev.ultreon.quantum.client.model.blockbench.BBColor,dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation,boolean,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = _BBAnimKeyFrame(arg0, arg1, arg2, _float.valueOf(arg3), arg4, arg5, _boolean.valueOf(arg6), arg7, arg8, arg9, arg10)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.toString()"""
        return str._wrap(super(BBAnimKeyFrame, self).toString())

    @overload
    def channel(self) -> 'BBAnimChannel':
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.channel()"""
        return 'BBAnimChannel'._wrap(super(BBAnimKeyFrame, self).channel())

    @overload
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.uuid()"""
        return 'UUID'._wrap(super(BBAnimKeyFrame, self).uuid()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation as _BBAnimation_Loop
_Loop = _BBAnimation_Loop.Loop
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
 
class Loop():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.Loop"""
 
    @staticmethod
    def _wrap(java_value: _Loop) -> 'Loop':
        return Loop(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Loop):
        """
        Dynamic initializer for Loop.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Loop__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Loop__wrapper":
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

    @staticmethod
    @overload
    def values() -> List['Loop']:
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop[] dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop.values()"""
        return List[Loop]._wrap(_Loop.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Loop':
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop.valueOf(java.lang.String)"""
        return Loop._wrap(_Loop.valueOf(arg0))


Loop.LOOP = Loop._wrap(_LOOP.LOOP)

Loop.ONCE = Loop._wrap(_ONCE.ONCE) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation
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
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation as _BBAnimInterpolation
_BBAnimInterpolation = _BBAnimInterpolation
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
 
class BBAnimInterpolation():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation"""
 
    @staticmethod
    def _wrap(java_value: _BBAnimInterpolation) -> 'BBAnimInterpolation':
        return BBAnimInterpolation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BBAnimInterpolation):
        """
        Dynamic initializer for BBAnimInterpolation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BBAnimInterpolation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BBAnimInterpolation__wrapper":
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BBAnimInterpolation':
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation.valueOf(java.lang.String)"""
        return BBAnimInterpolation._wrap(_BBAnimInterpolation.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['BBAnimInterpolation']:
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation[] dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation.values()"""
        return List[BBAnimInterpolation]._wrap(_BBAnimInterpolation.values())

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


BBAnimInterpolation.BEZIER = BBAnimInterpolation._wrap(_BEZIER.BEZIER)

BBAnimInterpolation.LINEAR = BBAnimInterpolation._wrap(_LINEAR.LINEAR)

BBAnimInterpolation.EASE_IN_OUT = BBAnimInterpolation._wrap(_EASE_IN_OUT.EASE_IN_OUT)

BBAnimInterpolation.EASE_IN = BBAnimInterpolation._wrap(_EASE_IN.EASE_IN)

BBAnimInterpolation.CATMULLROM = BBAnimInterpolation._wrap(_CATMULLROM.CATMULLROM)

BBAnimInterpolation.EASE_OUT = BBAnimInterpolation._wrap(_EASE_OUT.EASE_OUT) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type
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
import java.util.Optional as _Optional
_Optional = _Optional
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator as _BBAnimator_Type
_Type = _BBAnimator_Type.Type
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Type():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.Type"""
 
    @staticmethod
    def _wrap(java_value: _Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Type):
        """
        Dynamic initializer for Type.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Type__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Type__wrapper":
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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type[] dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type.values()"""
        return List[Type]._wrap(_Type.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(arg0))


Type.BONE = Type._wrap(_BONE.BONE)

Type.CUBE = Type._wrap(_CUBE.CUBE)