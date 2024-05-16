from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.model import blockbench
except ImportError:
    blockbench = __import_once__("pyquantum.client.model.blockbench")

import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator as __BBAnimator_Type
__Type = __BBAnimator_Type.Type
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator as __BBAnimator
__BBAnimator = __BBAnimator
import com.badlogic.gdx.graphics.g3d.model.Animation as __Animation
__Animation = __Animation
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = __import_once__("pygdx.graphics.g3d.model")

import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
import java.util.List as List
 
class BBAnimator():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator"""
 
    @staticmethod
    def __wrap(java_value: __BBAnimator) -> 'BBAnimator':
        return BBAnimator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBAnimator):
        """
        Dynamic initializer for BBAnimator.
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
    def build(self, arg0: 'Node', arg1: 'BBModelLoader', arg2: 'Animation', arg3: 'Map') -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.build(com.badlogic.gdx.graphics.g3d.model.Node,dev.ultreon.quantum.client.model.blockbench.BBModelLoader,com.badlogic.gdx.graphics.g3d.model.Animation,java.util.Map<com.badlogic.gdx.graphics.g3d.model.Node, com.badlogic.gdx.graphics.g3d.model.NodeAnimation>)"""
        return 'model.Animation'.__wrap(super(__BBAnimator, self).build(arg0, arg1, arg2, arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBAnimator, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.hashCode()"""
        return int.__wrap(super(BBAnimator, self).hashCode())

    @overload
    def __init__(self, arg0: str, arg1: 'Type', arg2: 'List'):
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator(java.lang.String,dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type,java.util.List<dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame>)"""
        val = __BBAnimator(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def keyFrames(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame> dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.keyFrames()"""
        return 'List'.__wrap(super(BBAnimator, self).keyFrames())

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
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.name()"""
        return str.__wrap(super(BBAnimator, self).name())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.toString()"""
        return str.__wrap(super(BBAnimator, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.type()"""
        return 'Type'.__wrap(super(BBAnimator, self).type())

 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.client.model import blockbench
except ImportError:
    blockbench = __import_once__("pyquantum.client.model.blockbench")

import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator as __BBAnimator_Type
__Type = __BBAnimator_Type.Type
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator as __BBAnimator
__BBAnimator = __BBAnimator
import com.badlogic.gdx.graphics.g3d.model.Animation as __Animation
__Animation = __Animation
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = __import_once__("pygdx.graphics.g3d.model")

import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
import java.util.List as List
 
class BBAnimator():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator"""
 
    @staticmethod
    def __wrap(java_value: __BBAnimator) -> 'BBAnimator':
        return BBAnimator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBAnimator):
        """
        Dynamic initializer for BBAnimator.
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
    def build(self, arg0: 'Node', arg1: 'BBModelLoader', arg2: 'Animation', arg3: 'Map') -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.build(com.badlogic.gdx.graphics.g3d.model.Node,dev.ultreon.quantum.client.model.blockbench.BBModelLoader,com.badlogic.gdx.graphics.g3d.model.Animation,java.util.Map<com.badlogic.gdx.graphics.g3d.model.Node, com.badlogic.gdx.graphics.g3d.model.NodeAnimation>)"""
        return 'model.Animation'.__wrap(super(__BBAnimator, self).build(arg0, arg1, arg2, arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBAnimator, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.hashCode()"""
        return int.__wrap(super(BBAnimator, self).hashCode())

    @overload
    def __init__(self, arg0: str, arg1: 'Type', arg2: 'List'):
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator(java.lang.String,dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type,java.util.List<dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame>)"""
        val = __BBAnimator(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def keyFrames(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame> dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.keyFrames()"""
        return 'List'.__wrap(super(BBAnimator, self).keyFrames())

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
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.name()"""
        return str.__wrap(super(BBAnimator, self).name())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.toString()"""
        return str.__wrap(super(BBAnimator, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def type(self) -> 'Type':
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.type()"""
        return 'Type'.__wrap(super(BBAnimator, self).type())

 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
from builtins import float
try:
    from pyquantum.client.model import blockbench
except ImportError:
    blockbench = __import_once__("pyquantum.client.model.blockbench")

import com.badlogic.gdx.graphics.g3d.model.Animation as __Animation
__Animation = __Animation
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = __import_once__("pygdx.graphics.g3d.model")

import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.String as __string
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation as __BBAnimation_Loop
__Loop = __BBAnimation_Loop.Loop
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation as __BBAnimation
__BBAnimation = __BBAnimation
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class BBAnimation():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation"""
 
    @staticmethod
    def __wrap(java_value: __BBAnimation) -> 'BBAnimation':
        return BBAnimation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBAnimation):
        """
        Dynamic initializer for BBAnimation.
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
    def animTimeUpdate(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.animTimeUpdate()"""
        return str.__wrap(super(BBAnimation, self).animTimeUpdate())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def blendWeight(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.blendWeight()"""
        return str.__wrap(super(BBAnimation, self).blendWeight())

    @overload
    def length(self) -> float:
        """public float dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.length()"""
        return float.__wrap(super(BBAnimation, self).length())

    @overload
    def override(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.override()"""
        return bool.__wrap(super(BBAnimation, self).override())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.toString()"""
        return str.__wrap(super(BBAnimation, self).toString())

    @overload
    def loopDelay(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.loopDelay()"""
        return str.__wrap(super(BBAnimation, self).loopDelay())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBAnimation, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.hashCode()"""
        return int.__wrap(super(BBAnimation, self).hashCode())

    @overload
    def selected(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.selected()"""
        return bool.__wrap(super(BBAnimation, self).selected())

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.name()"""
        return str.__wrap(super(BBAnimation, self).name())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def create(self, arg0: 'Map', arg1: 'BBModelLoader') -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.create(java.util.Map<java.util.UUID, com.badlogic.gdx.graphics.g3d.model.Node>,dev.ultreon.quantum.client.model.blockbench.BBModelLoader)"""
        return 'model.Animation'.__wrap(super(__BBAnimation, self).create(arg0, arg1))

    @overload
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.uuid()"""
        return 'UUID'.__wrap(super(BBAnimation, self).uuid())

    @overload
    def loop(self) -> 'Loop':
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.loop()"""
        return 'Loop'.__wrap(super(BBAnimation, self).loop())

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
    def startDelay(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.startDelay()"""
        return str.__wrap(super(BBAnimation, self).startDelay())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def snapping(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.snapping()"""
        return int.__wrap(super(BBAnimation, self).snapping())

    @overload
    def animators(self) -> 'Map':
        """public java.util.Map<java.util.UUID, dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator> dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.animators()"""
        return 'Map'.__wrap(super(BBAnimation, self).animators())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'UUID', arg1: str, arg2: 'Loop', arg3: bool, arg4: float, arg5: int, arg6: bool, arg7: str, arg8: str, arg9: str, arg10: str, arg11: 'Map'):
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation(java.util.UUID,java.lang.String,dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop,boolean,float,int,boolean,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.util.Map<java.util.UUID, dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator>)"""
        val = __BBAnimation(arg0, arg1, arg2, __boolean.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __boolean.valueOf(arg6), arg7, arg8, arg9, arg10, arg11)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel as __BBAnimChannel
__BBAnimChannel = __BBAnimChannel
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
 
class BBAnimChannel():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel"""
 
    @staticmethod
    def __wrap(java_value: __BBAnimChannel) -> 'BBAnimChannel':
        return BBAnimChannel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBAnimChannel):
        """
        Dynamic initializer for BBAnimChannel.
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
 
    # public static final dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel.POSITION
    POSITION: 'BBAnimChannel' = __wrap(__BBAnimChannel.POSITION)

    # public static final dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel.ROTATION
    ROTATION: 'BBAnimChannel' = __wrap(__BBAnimChannel.ROTATION)

    # public static final dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel.SCALE
    SCALE: 'BBAnimChannel' = __wrap(__BBAnimChannel.SCALE)


    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BBAnimChannel':
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel.valueOf(java.lang.String)"""
        return BBAnimChannel.__wrap(__BBAnimChannel.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['BBAnimChannel']:
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel[] dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel.values()"""
        return List[BBAnimChannel].__wrap(__BBAnimChannel.values())

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
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation as __BBAnimInterpolation
__BBAnimInterpolation = __BBAnimInterpolation
import java.lang.Boolean as __boolean
from builtins import type
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame as __BBAnimKeyFrame
__BBAnimKeyFrame = __BBAnimKeyFrame
try:
    from pyquantum.client.model import blockbench
except ImportError:
    blockbench = __import_once__("pyquantum.client.model.blockbench")

import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
import dev.ultreon.quantum.client.model.blockbench.BBColor as __BBColor
__BBColor = __BBColor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
from builtins import float
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel as __BBAnimChannel
__BBAnimChannel = __BBAnimChannel
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
 
class BBAnimKeyFrame():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame"""
 
    @staticmethod
    def __wrap(java_value: __BBAnimKeyFrame) -> 'BBAnimKeyFrame':
        return BBAnimKeyFrame(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBAnimKeyFrame):
        """
        Dynamic initializer for BBAnimKeyFrame.
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
    def bezierLinked(self) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.bezierLinked()"""
        return bool.__wrap(super(BBAnimKeyFrame, self).bezierLinked())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.hashCode()"""
        return int.__wrap(super(BBAnimKeyFrame, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.equals(java.lang.Object)"""
        return bool.__wrap(super(__BBAnimKeyFrame, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.toString()"""
        return str.__wrap(super(BBAnimKeyFrame, self).toString())

    @overload
    def bezierRightTime(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.bezierRightTime()"""
        return 'math.Vector3'.__wrap(super(BBAnimKeyFrame, self).bezierRightTime())

    @overload
    def bezierLeftValue(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.bezierLeftValue()"""
        return 'math.Vector3'.__wrap(super(BBAnimKeyFrame, self).bezierLeftValue())

    @overload
    def dataPoints(self) -> 'List':
        """public java.util.List<com.badlogic.gdx.math.Vector3> dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.dataPoints()"""
        return 'List'.__wrap(super(BBAnimKeyFrame, self).dataPoints())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def color(self) -> 'blockbench.BBColor':
        """public dev.ultreon.quantum.client.model.blockbench.BBColor dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.color()"""
        return 'blockbench.BBColor'.__wrap(super(BBAnimKeyFrame, self).color())

    @overload
    def interpolation(self) -> 'BBAnimInterpolation':
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.interpolation()"""
        return 'BBAnimInterpolation'.__wrap(super(BBAnimKeyFrame, self).interpolation())

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
    def __init__(self, arg0: 'BBAnimChannel', arg1: 'List', arg2: 'UUID', arg3: float, arg4: 'BBColor', arg5: 'BBAnimInterpolation', arg6: bool, arg7: 'Vector3', arg8: 'Vector3', arg9: 'Vector3', arg10: 'Vector3'):
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame(dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel,java.util.List<com.badlogic.gdx.math.Vector3>,java.util.UUID,float,dev.ultreon.quantum.client.model.blockbench.BBColor,dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation,boolean,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = __BBAnimKeyFrame(arg0, arg1, arg2, __float.valueOf(arg3), arg4, arg5, __boolean.valueOf(arg6), arg7, arg8, arg9, arg10)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def bezierLeftTime(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.bezierLeftTime()"""
        return 'math.Vector3'.__wrap(super(BBAnimKeyFrame, self).bezierLeftTime())

    @overload
    def bezierRightValue(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.bezierRightValue()"""
        return 'math.Vector3'.__wrap(super(BBAnimKeyFrame, self).bezierRightValue())

    @overload
    def channel(self) -> 'BBAnimChannel':
        """public dev.ultreon.quantum.client.model.blockbench.anim.BBAnimChannel dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.channel()"""
        return 'BBAnimChannel'.__wrap(super(BBAnimKeyFrame, self).channel())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def time(self) -> float:
        """public float dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.time()"""
        return float.__wrap(super(BBAnimKeyFrame, self).time())

    @overload
    def uuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.client.model.blockbench.anim.BBAnimKeyFrame.uuid()"""
        return 'UUID'.__wrap(super(BBAnimKeyFrame, self).uuid()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop
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
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation as __BBAnimation_Loop
__Loop = __BBAnimation_Loop.Loop
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Loop():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation.Loop"""
 
    @staticmethod
    def __wrap(java_value: __Loop) -> 'Loop':
        return Loop(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Loop):
        """
        Dynamic initializer for Loop.
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
 
    # public static final dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop.ONCE
    ONCE: 'Loop' = __wrap(__Loop.ONCE)

    # public static final dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop.LOOP
    LOOP: 'Loop' = __wrap(__Loop.LOOP)


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
    def values() -> List['Loop']:
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop[] dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop.values()"""
        return List[Loop].__wrap(__Loop.values())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Loop':
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop dev.ultreon.quantum.client.model.blockbench.anim.BBAnimation$Loop.valueOf(java.lang.String)"""
        return Loop.__wrap(__Loop.valueOf(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation
from builtins import str
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation as __BBAnimInterpolation
__BBAnimInterpolation = __BBAnimInterpolation
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
 
class BBAnimInterpolation():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation"""
 
    @staticmethod
    def __wrap(java_value: __BBAnimInterpolation) -> 'BBAnimInterpolation':
        return BBAnimInterpolation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BBAnimInterpolation):
        """
        Dynamic initializer for BBAnimInterpolation.
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
 
    # public static final dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation.CATMULLROM
    CATMULLROM: 'BBAnimInterpolation' = __wrap(__BBAnimInterpolation.CATMULLROM)

    # public static final dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation.LINEAR
    LINEAR: 'BBAnimInterpolation' = __wrap(__BBAnimInterpolation.LINEAR)

    # public static final dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation.EASE_IN_OUT
    EASE_IN_OUT: 'BBAnimInterpolation' = __wrap(__BBAnimInterpolation.EASE_IN_OUT)

    # public static final dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation.EASE_OUT
    EASE_OUT: 'BBAnimInterpolation' = __wrap(__BBAnimInterpolation.EASE_OUT)

    # public static final dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation.BEZIER
    BEZIER: 'BBAnimInterpolation' = __wrap(__BBAnimInterpolation.BEZIER)

    # public static final dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation.EASE_IN
    EASE_IN: 'BBAnimInterpolation' = __wrap(__BBAnimInterpolation.EASE_IN)


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
    def valueOf(arg0: str) -> 'BBAnimInterpolation':
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation.valueOf(java.lang.String)"""
        return BBAnimInterpolation.__wrap(__BBAnimInterpolation.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['BBAnimInterpolation']:
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation[] dev.ultreon.quantum.client.model.blockbench.anim.BBAnimInterpolation.values()"""
        return List[BBAnimInterpolation].__wrap(__BBAnimInterpolation.values())

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
 
 
# CLASS: dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator as __BBAnimator_Type
__Type = __BBAnimator_Type.Type
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
 
class Type():
    """dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator.Type"""
 
    @staticmethod
    def __wrap(java_value: __Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Type):
        """
        Dynamic initializer for Type.
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
 
    # public static final dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type.BONE
    BONE: 'Type' = __wrap(__Type.BONE)

    # public static final dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type.CUBE
    CUBE: 'Type' = __wrap(__Type.CUBE)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type[] dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type.values()"""
        return List[Type].__wrap(__Type.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type dev.ultreon.quantum.client.model.blockbench.anim.BBAnimator$Type.valueOf(java.lang.String)"""
        return Type.__wrap(__Type.valueOf(arg0))

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