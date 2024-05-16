from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.physics.box2d.joints.GearJointDef as __GearJointDef
__GearJointDef = __GearJointDef
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GearJointDef():
    """com.badlogic.gdx.physics.box2d.joints.GearJointDef"""
 
    @staticmethod
    def __wrap(java_value: __GearJointDef) -> 'GearJointDef':
        return GearJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GearJointDef):
        """
        Dynamic initializer for GearJointDef.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.GearJointDef()"""
        val = __GearJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.GearJointDef()"""
        val = __GearJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.GearJointDef
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.physics.box2d.joints.GearJointDef as __GearJointDef
__GearJointDef = __GearJointDef
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GearJointDef():
    """com.badlogic.gdx.physics.box2d.joints.GearJointDef"""
 
    @staticmethod
    def __wrap(java_value: __GearJointDef) -> 'GearJointDef':
        return GearJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GearJointDef):
        """
        Dynamic initializer for GearJointDef.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.GearJointDef()"""
        val = __GearJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.GearJointDef()"""
        val = __GearJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.GearJointDef 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.RopeJointDef
from builtins import str
import com.badlogic.gdx.physics.box2d.joints.RopeJointDef as __RopeJointDef
__RopeJointDef = __RopeJointDef
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RopeJointDef():
    """com.badlogic.gdx.physics.box2d.joints.RopeJointDef"""
 
    @staticmethod
    def __wrap(java_value: __RopeJointDef) -> 'RopeJointDef':
        return RopeJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RopeJointDef):
        """
        Dynamic initializer for RopeJointDef.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.RopeJointDef()"""
        val = __RopeJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.RopeJointDef()"""
        val = __RopeJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.DistanceJoint
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef_JointType
__JointType = __JointDef_JointType.JointType
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
from builtins import object
import com.badlogic.gdx.physics.box2d.Joint as __Joint
__Joint = __Joint
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.physics.box2d.joints.DistanceJoint as __DistanceJoint
__DistanceJoint = __DistanceJoint
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DistanceJoint():
    """com.badlogic.gdx.physics.box2d.joints.DistanceJoint"""
 
    @staticmethod
    def __wrap(java_value: __DistanceJoint) -> 'DistanceJoint':
        return DistanceJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DistanceJoint):
        """
        Dynamic initializer for DistanceJoint.
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
    def setDampingRatio(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.DistanceJoint.setDampingRatio(float)"""
        super(__DistanceJoint, self).setDampingRatio(__float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.DistanceJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = __DistanceJoint(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getFrequency(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.DistanceJoint.getFrequency()"""
        return float.__wrap(super(DistanceJoint, self).getFrequency())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLength(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.DistanceJoint.setLength(float)"""
        super(__DistanceJoint, self).setLength(__float.valueOf(arg0))

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool.__wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(__box2d.Joint, self).setUserData(arg0)

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object.__wrap(super(box2d.Joint, self).getUserData())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'.__wrap(super(box2d.Joint, self).getType())

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.DistanceJoint.getLocalAnchorB()"""
        return 'math.Vector2'.__wrap(super(DistanceJoint, self).getLocalAnchorB())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def setFrequency(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.DistanceJoint.setFrequency(float)"""
        super(__DistanceJoint, self).setFrequency(__float.valueOf(arg0))

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'.__wrap(super(__box2d.Joint, self).getReactionForce(__float.valueOf(arg0)))

    @overload
    def getLength(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.DistanceJoint.getLength()"""
        return float.__wrap(super(DistanceJoint, self).getLength())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float.__wrap(super(__box2d.Joint, self).getReactionTorque(__float.valueOf(arg0)))

    @overload
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.DistanceJoint.getLocalAnchorA()"""
        return 'math.Vector2'.__wrap(super(DistanceJoint, self).getLocalAnchorA())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorB())

    @overload
    def getDampingRatio(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.DistanceJoint.getDampingRatio()"""
        return float.__wrap(super(DistanceJoint, self).getDampingRatio())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool.__wrap(super(box2d.Joint, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.WheelJointDef
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.physics.box2d.joints.WheelJointDef as __WheelJointDef
__WheelJointDef = __WheelJointDef
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WheelJointDef():
    """com.badlogic.gdx.physics.box2d.joints.WheelJointDef"""
 
    @staticmethod
    def __wrap(java_value: __WheelJointDef) -> 'WheelJointDef':
        return WheelJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WheelJointDef):
        """
        Dynamic initializer for WheelJointDef.
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
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.WheelJointDef()"""
        val = __WheelJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.WheelJointDef()"""
        val = __WheelJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def initialize(self, arg0: 'Body', arg1: 'Body', arg2: 'Vector2', arg3: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.WheelJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(__WheelJointDef, self).initialize(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.MotorJoint
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.joints.MotorJoint as __MotorJoint
__MotorJoint = __MotorJoint
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef_JointType
__JointType = __JointDef_JointType.JointType
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
from builtins import object
import com.badlogic.gdx.physics.box2d.Joint as __Joint
__Joint = __Joint
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MotorJoint():
    """com.badlogic.gdx.physics.box2d.joints.MotorJoint"""
 
    @staticmethod
    def __wrap(java_value: __MotorJoint) -> 'MotorJoint':
        return MotorJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MotorJoint):
        """
        Dynamic initializer for MotorJoint.
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
    def setMaxForce(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MotorJoint.setMaxForce(float)"""
        super(__MotorJoint, self).setMaxForce(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getMaxTorque(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MotorJoint.getMaxTorque()"""
        return float.__wrap(super(MotorJoint, self).getMaxTorque())

    @overload
    def setMaxTorque(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MotorJoint.setMaxTorque(float)"""
        super(__MotorJoint, self).setMaxTorque(__float.valueOf(arg0))

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool.__wrap(super(box2d.Joint, self).getCollideConnected())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.MotorJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = __MotorJoint(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(__box2d.Joint, self).setUserData(arg0)

    @overload
    def setAngularOffset(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MotorJoint.setAngularOffset(float)"""
        super(__MotorJoint, self).setAngularOffset(__float.valueOf(arg0))

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object.__wrap(super(box2d.Joint, self).getUserData())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'.__wrap(super(box2d.Joint, self).getType())

    @overload
    def getMaxForce(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MotorJoint.getMaxForce()"""
        return float.__wrap(super(MotorJoint, self).getMaxForce())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def getCorrectionFactor(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MotorJoint.getCorrectionFactor()"""
        return float.__wrap(super(MotorJoint, self).getCorrectionFactor())

    @overload
    def getAngularOffset(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MotorJoint.getAngularOffset()"""
        return float.__wrap(super(MotorJoint, self).getAngularOffset())

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'.__wrap(super(__box2d.Joint, self).getReactionForce(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setLinearOffset(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.MotorJoint.setLinearOffset(com.badlogic.gdx.math.Vector2)"""
        super(__MotorJoint, self).setLinearOffset(arg0)

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float.__wrap(super(__box2d.Joint, self).getReactionTorque(__float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setCorrectionFactor(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MotorJoint.setCorrectionFactor(float)"""
        super(__MotorJoint, self).setCorrectionFactor(__float.valueOf(arg0))

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool.__wrap(super(box2d.Joint, self).isActive())

    @overload
    def getLinearOffset(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.MotorJoint.getLinearOffset()"""
        return 'math.Vector2'.__wrap(super(MotorJoint, self).getLinearOffset())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.PrismaticJointDef
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.physics.box2d.joints.PrismaticJointDef as __PrismaticJointDef
__PrismaticJointDef = __PrismaticJointDef
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PrismaticJointDef():
    """com.badlogic.gdx.physics.box2d.joints.PrismaticJointDef"""
 
    @staticmethod
    def __wrap(java_value: __PrismaticJointDef) -> 'PrismaticJointDef':
        return PrismaticJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PrismaticJointDef):
        """
        Dynamic initializer for PrismaticJointDef.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.PrismaticJointDef()"""
        val = __PrismaticJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.PrismaticJointDef()"""
        val = __PrismaticJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def initialize(self, arg0: 'Body', arg1: 'Body', arg2: 'Vector2', arg3: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.PrismaticJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(__PrismaticJointDef, self).initialize(arg0, arg1, arg2, arg3) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.WeldJoint
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

from builtins import type
import com.badlogic.gdx.physics.box2d.joints.WeldJoint as __WeldJoint
__WeldJoint = __WeldJoint
from builtins import float
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef_JointType
__JointType = __JointDef_JointType.JointType
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
from builtins import object
import com.badlogic.gdx.physics.box2d.Joint as __Joint
__Joint = __Joint
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WeldJoint():
    """com.badlogic.gdx.physics.box2d.joints.WeldJoint"""
 
    @staticmethod
    def __wrap(java_value: __WeldJoint) -> 'WeldJoint':
        return WeldJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WeldJoint):
        """
        Dynamic initializer for WeldJoint.
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
    def setDampingRatio(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.WeldJoint.setDampingRatio(float)"""
        super(__WeldJoint, self).setDampingRatio(__float.valueOf(arg0))

    @overload
    def getFrequency(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WeldJoint.getFrequency()"""
        return float.__wrap(super(WeldJoint, self).getFrequency())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool.__wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.WeldJoint.getLocalAnchorB()"""
        return 'math.Vector2'.__wrap(super(WeldJoint, self).getLocalAnchorB())

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(__box2d.Joint, self).setUserData(arg0)

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object.__wrap(super(box2d.Joint, self).getUserData())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'.__wrap(super(box2d.Joint, self).getType())

    @overload
    def getReferenceAngle(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WeldJoint.getReferenceAngle()"""
        return float.__wrap(super(WeldJoint, self).getReferenceAngle())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.WeldJoint.getLocalAnchorA()"""
        return 'math.Vector2'.__wrap(super(WeldJoint, self).getLocalAnchorA())

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'.__wrap(super(__box2d.Joint, self).getReactionForce(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.WeldJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = __WeldJoint(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float.__wrap(super(__box2d.Joint, self).getReactionTorque(__float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorB())

    @overload
    def setFrequency(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.WeldJoint.setFrequency(float)"""
        super(__WeldJoint, self).setFrequency(__float.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool.__wrap(super(box2d.Joint, self).isActive())

    @overload
    def getDampingRatio(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WeldJoint.getDampingRatio()"""
        return float.__wrap(super(WeldJoint, self).getDampingRatio())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.MouseJoint
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef_JointType
__JointType = __JointDef_JointType.JointType
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
from builtins import object
import com.badlogic.gdx.physics.box2d.joints.MouseJoint as __MouseJoint
__MouseJoint = __MouseJoint
import com.badlogic.gdx.physics.box2d.Joint as __Joint
__Joint = __Joint
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MouseJoint():
    """com.badlogic.gdx.physics.box2d.joints.MouseJoint"""
 
    @staticmethod
    def __wrap(java_value: __MouseJoint) -> 'MouseJoint':
        return MouseJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MouseJoint):
        """
        Dynamic initializer for MouseJoint.
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

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool.__wrap(super(box2d.Joint, self).getCollideConnected())

    @overload
    def getDampingRatio(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MouseJoint.getDampingRatio()"""
        return float.__wrap(super(MouseJoint, self).getDampingRatio())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(__box2d.Joint, self).setUserData(arg0)

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object.__wrap(super(box2d.Joint, self).getUserData())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setMaxForce(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MouseJoint.setMaxForce(float)"""
        super(__MouseJoint, self).setMaxForce(__float.valueOf(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'.__wrap(super(box2d.Joint, self).getType())

    @overload
    def getMaxForce(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MouseJoint.getMaxForce()"""
        return float.__wrap(super(MouseJoint, self).getMaxForce())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setDampingRatio(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MouseJoint.setDampingRatio(float)"""
        super(__MouseJoint, self).setDampingRatio(__float.valueOf(arg0))

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def setTarget(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.MouseJoint.setTarget(com.badlogic.gdx.math.Vector2)"""
        super(__MouseJoint, self).setTarget(arg0)

    @overload
    def setFrequency(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MouseJoint.setFrequency(float)"""
        super(__MouseJoint, self).setFrequency(__float.valueOf(arg0))

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'.__wrap(super(__box2d.Joint, self).getReactionForce(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float.__wrap(super(__box2d.Joint, self).getReactionTorque(__float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorB())

    @overload
    def getTarget(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.MouseJoint.getTarget()"""
        return 'math.Vector2'.__wrap(super(MouseJoint, self).getTarget())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool.__wrap(super(box2d.Joint, self).isActive())

    @overload
    def getFrequency(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MouseJoint.getFrequency()"""
        return float.__wrap(super(MouseJoint, self).getFrequency())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.MouseJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = __MouseJoint(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.MouseJointDef
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.physics.box2d.joints.MouseJointDef as __MouseJointDef
__MouseJointDef = __MouseJointDef
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MouseJointDef():
    """com.badlogic.gdx.physics.box2d.joints.MouseJointDef"""
 
    @staticmethod
    def __wrap(java_value: __MouseJointDef) -> 'MouseJointDef':
        return MouseJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MouseJointDef):
        """
        Dynamic initializer for MouseJointDef.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.MouseJointDef()"""
        val = __MouseJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.MouseJointDef()"""
        val = __MouseJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.MotorJointDef
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.physics.box2d.joints.MotorJointDef as __MotorJointDef
__MotorJointDef = __MotorJointDef
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MotorJointDef():
    """com.badlogic.gdx.physics.box2d.joints.MotorJointDef"""
 
    @staticmethod
    def __wrap(java_value: __MotorJointDef) -> 'MotorJointDef':
        return MotorJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MotorJointDef):
        """
        Dynamic initializer for MotorJointDef.
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
    def initialize(self, arg0: 'Body', arg1: 'Body'):
        """public void com.badlogic.gdx.physics.box2d.joints.MotorJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body)"""
        super(__MotorJointDef, self).initialize(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.MotorJointDef()"""
        val = __MotorJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.MotorJointDef()"""
        val = __MotorJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.PulleyJointDef
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.physics.box2d.joints.PulleyJointDef as __PulleyJointDef
__PulleyJointDef = __PulleyJointDef
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PulleyJointDef():
    """com.badlogic.gdx.physics.box2d.joints.PulleyJointDef"""
 
    @staticmethod
    def __wrap(java_value: __PulleyJointDef) -> 'PulleyJointDef':
        return PulleyJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PulleyJointDef):
        """
        Dynamic initializer for PulleyJointDef.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.PulleyJointDef()"""
        val = __PulleyJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.PulleyJointDef()"""
        val = __PulleyJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initialize(self, arg0: 'Body', arg1: 'Body', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2', arg5: 'Vector2', arg6: float):
        """public void com.badlogic.gdx.physics.box2d.joints.PulleyJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        super(__PulleyJointDef, self).initialize(arg0, arg1, arg2, arg3, arg4, arg5, __float.valueOf(arg6)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.GearJoint
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef_JointType
__JointType = __JointDef_JointType.JointType
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
from builtins import object
import com.badlogic.gdx.physics.box2d.Joint as __Joint
__Joint = __Joint
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
import com.badlogic.gdx.physics.box2d.joints.GearJoint as __GearJoint
__GearJoint = __GearJoint
from builtins import bool
from builtins import int
 
class GearJoint():
    """com.badlogic.gdx.physics.box2d.joints.GearJoint"""
 
    @staticmethod
    def __wrap(java_value: __GearJoint) -> 'GearJoint':
        return GearJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GearJoint):
        """
        Dynamic initializer for GearJoint.
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
    def getJoint2(self) -> 'box2d.Joint':
        """public com.badlogic.gdx.physics.box2d.Joint com.badlogic.gdx.physics.box2d.joints.GearJoint.getJoint2()"""
        return 'box2d.Joint'.__wrap(super(GearJoint, self).getJoint2())

    @overload
    def setRatio(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.GearJoint.setRatio(float)"""
        super(__GearJoint, self).setRatio(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getJoint1(self) -> 'box2d.Joint':
        """public com.badlogic.gdx.physics.box2d.Joint com.badlogic.gdx.physics.box2d.joints.GearJoint.getJoint1()"""
        return 'box2d.Joint'.__wrap(super(GearJoint, self).getJoint1())

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool.__wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(__box2d.Joint, self).setUserData(arg0)

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object.__wrap(super(box2d.Joint, self).getUserData())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'.__wrap(super(box2d.Joint, self).getType())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'.__wrap(super(__box2d.Joint, self).getReactionForce(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float.__wrap(super(__box2d.Joint, self).getReactionTorque(__float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool.__wrap(super(box2d.Joint, self).isActive())

    @overload
    def __init__(self, arg0: 'World', arg1: int, arg2: 'Joint', arg3: 'Joint'):
        """public com.badlogic.gdx.physics.box2d.joints.GearJoint(com.badlogic.gdx.physics.box2d.World,long,com.badlogic.gdx.physics.box2d.Joint,com.badlogic.gdx.physics.box2d.Joint)"""
        val = __GearJoint(arg0, __long.valueOf(arg1), arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getRatio(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.GearJoint.getRatio()"""
        return float.__wrap(super(GearJoint, self).getRatio()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.DistanceJointDef
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.physics.box2d.joints.DistanceJointDef as __DistanceJointDef
__DistanceJointDef = __DistanceJointDef
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DistanceJointDef():
    """com.badlogic.gdx.physics.box2d.joints.DistanceJointDef"""
 
    @staticmethod
    def __wrap(java_value: __DistanceJointDef) -> 'DistanceJointDef':
        return DistanceJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DistanceJointDef):
        """
        Dynamic initializer for DistanceJointDef.
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
    def initialize(self, arg0: 'Body', arg1: 'Body', arg2: 'Vector2', arg3: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.DistanceJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(__DistanceJointDef, self).initialize(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.DistanceJointDef()"""
        val = __DistanceJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.DistanceJointDef()"""
        val = __DistanceJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.WheelJoint
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef_JointType
__JointType = __JointDef_JointType.JointType
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
from builtins import object
import com.badlogic.gdx.physics.box2d.Joint as __Joint
__Joint = __Joint
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import com.badlogic.gdx.physics.box2d.joints.WheelJoint as __WheelJoint
__WheelJoint = __WheelJoint
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WheelJoint():
    """com.badlogic.gdx.physics.box2d.joints.WheelJoint"""
 
    @staticmethod
    def __wrap(java_value: __WheelJoint) -> 'WheelJoint':
        return WheelJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WheelJoint):
        """
        Dynamic initializer for WheelJoint.
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
    def getMotorTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getMotorTorque(float)"""
        return float.__wrap(super(__WheelJoint, self).getMotorTorque(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setMaxMotorTorque(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.WheelJoint.setMaxMotorTorque(float)"""
        super(__WheelJoint, self).setMaxMotorTorque(__float.valueOf(arg0))

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.WheelJoint.getLocalAnchorB()"""
        return 'math.Vector2'.__wrap(super(WheelJoint, self).getLocalAnchorB())

    @overload
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.WheelJoint.getLocalAnchorA()"""
        return 'math.Vector2'.__wrap(super(WheelJoint, self).getLocalAnchorA())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setSpringDampingRatio(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.WheelJoint.setSpringDampingRatio(float)"""
        super(__WheelJoint, self).setSpringDampingRatio(__float.valueOf(arg0))

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool.__wrap(super(box2d.Joint, self).getCollideConnected())

    @overload
    def getMotorSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getMotorSpeed()"""
        return float.__wrap(super(WheelJoint, self).getMotorSpeed())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(__box2d.Joint, self).setUserData(arg0)

    @overload
    def getJointSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getJointSpeed()"""
        return float.__wrap(super(WheelJoint, self).getJointSpeed())

    @overload
    def setMotorSpeed(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.WheelJoint.setMotorSpeed(float)"""
        super(__WheelJoint, self).setMotorSpeed(__float.valueOf(arg0))

    @overload
    def getLocalAxisA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.WheelJoint.getLocalAxisA()"""
        return 'math.Vector2'.__wrap(super(WheelJoint, self).getLocalAxisA())

    @overload
    def isMotorEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.joints.WheelJoint.isMotorEnabled()"""
        return bool.__wrap(super(WheelJoint, self).isMotorEnabled())

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object.__wrap(super(box2d.Joint, self).getUserData())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'.__wrap(super(box2d.Joint, self).getType())

    @overload
    def getSpringDampingRatio(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getSpringDampingRatio()"""
        return float.__wrap(super(WheelJoint, self).getSpringDampingRatio())

    @overload
    def getSpringFrequencyHz(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getSpringFrequencyHz()"""
        return float.__wrap(super(WheelJoint, self).getSpringFrequencyHz())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setSpringFrequencyHz(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.WheelJoint.setSpringFrequencyHz(float)"""
        super(__WheelJoint, self).setSpringFrequencyHz(__float.valueOf(arg0))

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'.__wrap(super(__box2d.Joint, self).getReactionForce(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.WheelJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = __WheelJoint(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float.__wrap(super(__box2d.Joint, self).getReactionTorque(__float.valueOf(arg0)))

    @overload
    def enableMotor(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.joints.WheelJoint.enableMotor(boolean)"""
        super(__WheelJoint, self).enableMotor(__boolean.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorB())

    @overload
    def getMaxMotorTorque(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getMaxMotorTorque()"""
        return float.__wrap(super(WheelJoint, self).getMaxMotorTorque())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool.__wrap(super(box2d.Joint, self).isActive())

    @overload
    def getJointTranslation(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getJointTranslation()"""
        return float.__wrap(super(WheelJoint, self).getJointTranslation())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.RevoluteJointDef
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.physics.box2d.joints.RevoluteJointDef as __RevoluteJointDef
__RevoluteJointDef = __RevoluteJointDef
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RevoluteJointDef():
    """com.badlogic.gdx.physics.box2d.joints.RevoluteJointDef"""
 
    @staticmethod
    def __wrap(java_value: __RevoluteJointDef) -> 'RevoluteJointDef':
        return RevoluteJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RevoluteJointDef):
        """
        Dynamic initializer for RevoluteJointDef.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.RevoluteJointDef()"""
        val = __RevoluteJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.RevoluteJointDef()"""
        val = __RevoluteJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
    def initialize(self, arg0: 'Body', arg1: 'Body', arg2: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.RevoluteJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2)"""
        super(__RevoluteJointDef, self).initialize(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.PrismaticJoint
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

from builtins import type
import com.badlogic.gdx.physics.box2d.joints.PrismaticJoint as __PrismaticJoint
__PrismaticJoint = __PrismaticJoint
from builtins import float
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef_JointType
__JointType = __JointDef_JointType.JointType
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
from builtins import object
import com.badlogic.gdx.physics.box2d.Joint as __Joint
__Joint = __Joint
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PrismaticJoint():
    """com.badlogic.gdx.physics.box2d.joints.PrismaticJoint"""
 
    @staticmethod
    def __wrap(java_value: __PrismaticJoint) -> 'PrismaticJoint':
        return PrismaticJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PrismaticJoint):
        """
        Dynamic initializer for PrismaticJoint.
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
    def enableMotor(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.enableMotor(boolean)"""
        super(__PrismaticJoint, self).enableMotor(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getJointTranslation(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getJointTranslation()"""
        return float.__wrap(super(PrismaticJoint, self).getJointTranslation())

    @overload
    def getJointSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getJointSpeed()"""
        return float.__wrap(super(PrismaticJoint, self).getJointSpeed())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.PrismaticJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = __PrismaticJoint(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isMotorEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.isMotorEnabled()"""
        return bool.__wrap(super(PrismaticJoint, self).isMotorEnabled())

    @overload
    def getLowerLimit(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getLowerLimit()"""
        return float.__wrap(super(PrismaticJoint, self).getLowerLimit())

    @overload
    def getMotorSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getMotorSpeed()"""
        return float.__wrap(super(PrismaticJoint, self).getMotorSpeed())

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorA())

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getLocalAnchorB()"""
        return 'math.Vector2'.__wrap(super(PrismaticJoint, self).getLocalAnchorB())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool.__wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(__box2d.Joint, self).setUserData(arg0)

    @overload
    def setMotorSpeed(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.setMotorSpeed(float)"""
        super(__PrismaticJoint, self).setMotorSpeed(__float.valueOf(arg0))

    @overload
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getLocalAnchorA()"""
        return 'math.Vector2'.__wrap(super(PrismaticJoint, self).getLocalAnchorA())

    @overload
    def getReferenceAngle(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getReferenceAngle()"""
        return float.__wrap(super(PrismaticJoint, self).getReferenceAngle())

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object.__wrap(super(box2d.Joint, self).getUserData())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'.__wrap(super(box2d.Joint, self).getType())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setLimits(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.setLimits(float,float)"""
        super(__PrismaticJoint, self).setLimits(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def setMaxMotorForce(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.setMaxMotorForce(float)"""
        super(__PrismaticJoint, self).setMaxMotorForce(__float.valueOf(arg0))

    @overload
    def getMaxMotorForce(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getMaxMotorForce()"""
        return float.__wrap(super(PrismaticJoint, self).getMaxMotorForce())

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'.__wrap(super(__box2d.Joint, self).getReactionForce(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float.__wrap(super(__box2d.Joint, self).getReactionTorque(__float.valueOf(arg0)))

    @overload
    def enableLimit(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.enableLimit(boolean)"""
        super(__PrismaticJoint, self).enableLimit(__boolean.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getLocalAxisA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getLocalAxisA()"""
        return 'math.Vector2'.__wrap(super(PrismaticJoint, self).getLocalAxisA())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool.__wrap(super(box2d.Joint, self).isActive())

    @overload
    def isLimitEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.isLimitEnabled()"""
        return bool.__wrap(super(PrismaticJoint, self).isLimitEnabled())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getUpperLimit(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getUpperLimit()"""
        return float.__wrap(super(PrismaticJoint, self).getUpperLimit())

    @overload
    def getMotorForce(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getMotorForce(float)"""
        return float.__wrap(super(__PrismaticJoint, self).getMotorForce(__float.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.FrictionJoint
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

from builtins import type
import com.badlogic.gdx.physics.box2d.joints.FrictionJoint as __FrictionJoint
__FrictionJoint = __FrictionJoint
from builtins import float
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef_JointType
__JointType = __JointDef_JointType.JointType
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
from builtins import object
import com.badlogic.gdx.physics.box2d.Joint as __Joint
__Joint = __Joint
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FrictionJoint():
    """com.badlogic.gdx.physics.box2d.joints.FrictionJoint"""
 
    @staticmethod
    def __wrap(java_value: __FrictionJoint) -> 'FrictionJoint':
        return FrictionJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FrictionJoint):
        """
        Dynamic initializer for FrictionJoint.
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
    def setMaxForce(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.FrictionJoint.setMaxForce(float)"""
        super(__FrictionJoint, self).setMaxForce(__float.valueOf(arg0))

    @overload
    def getMaxTorque(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.FrictionJoint.getMaxTorque()"""
        return float.__wrap(super(FrictionJoint, self).getMaxTorque())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getMaxForce(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.FrictionJoint.getMaxForce()"""
        return float.__wrap(super(FrictionJoint, self).getMaxForce())

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool.__wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(__box2d.Joint, self).setUserData(arg0)

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object.__wrap(super(box2d.Joint, self).getUserData())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'.__wrap(super(box2d.Joint, self).getType())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.FrictionJoint.getLocalAnchorA()"""
        return 'math.Vector2'.__wrap(super(FrictionJoint, self).getLocalAnchorA())

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'.__wrap(super(__box2d.Joint, self).getReactionForce(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.FrictionJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = __FrictionJoint(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float.__wrap(super(__box2d.Joint, self).getReactionTorque(__float.valueOf(arg0)))

    @overload
    def setMaxTorque(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.FrictionJoint.setMaxTorque(float)"""
        super(__FrictionJoint, self).setMaxTorque(__float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool.__wrap(super(box2d.Joint, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.FrictionJoint.getLocalAnchorB()"""
        return 'math.Vector2'.__wrap(super(FrictionJoint, self).getLocalAnchorB()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.FrictionJointDef
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.physics.box2d.joints.FrictionJointDef as __FrictionJointDef
__FrictionJointDef = __FrictionJointDef
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FrictionJointDef():
    """com.badlogic.gdx.physics.box2d.joints.FrictionJointDef"""
 
    @staticmethod
    def __wrap(java_value: __FrictionJointDef) -> 'FrictionJointDef':
        return FrictionJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FrictionJointDef):
        """
        Dynamic initializer for FrictionJointDef.
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
    def initialize(self, arg0: 'Body', arg1: 'Body', arg2: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.FrictionJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2)"""
        super(__FrictionJointDef, self).initialize(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.FrictionJointDef()"""
        val = __FrictionJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.FrictionJointDef()"""
        val = __FrictionJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.PulleyJoint
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.physics.box2d.joints.PulleyJoint as __PulleyJoint
__PulleyJoint = __PulleyJoint
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef_JointType
__JointType = __JointDef_JointType.JointType
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
from builtins import object
import com.badlogic.gdx.physics.box2d.Joint as __Joint
__Joint = __Joint
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PulleyJoint():
    """com.badlogic.gdx.physics.box2d.joints.PulleyJoint"""
 
    @staticmethod
    def __wrap(java_value: __PulleyJoint) -> 'PulleyJoint':
        return PulleyJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PulleyJoint):
        """
        Dynamic initializer for PulleyJoint.
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
    def getLength1(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PulleyJoint.getLength1()"""
        return float.__wrap(super(PulleyJoint, self).getLength1())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getRatio(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PulleyJoint.getRatio()"""
        return float.__wrap(super(PulleyJoint, self).getRatio())

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool.__wrap(super(box2d.Joint, self).getCollideConnected())

    @overload
    def getGroundAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.PulleyJoint.getGroundAnchorB()"""
        return 'math.Vector2'.__wrap(super(PulleyJoint, self).getGroundAnchorB())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(__box2d.Joint, self).setUserData(arg0)

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object.__wrap(super(box2d.Joint, self).getUserData())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'.__wrap(super(box2d.Joint, self).getType())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getLength2(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PulleyJoint.getLength2()"""
        return float.__wrap(super(PulleyJoint, self).getLength2())

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.PulleyJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = __PulleyJoint(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'.__wrap(super(__box2d.Joint, self).getReactionForce(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float.__wrap(super(__box2d.Joint, self).getReactionTorque(__float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool.__wrap(super(box2d.Joint, self).isActive())

    @overload
    def getGroundAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.PulleyJoint.getGroundAnchorA()"""
        return 'math.Vector2'.__wrap(super(PulleyJoint, self).getGroundAnchorA())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.RevoluteJoint
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef_JointType
__JointType = __JointDef_JointType.JointType
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
from builtins import object
import com.badlogic.gdx.physics.box2d.joints.RevoluteJoint as __RevoluteJoint
__RevoluteJoint = __RevoluteJoint
import com.badlogic.gdx.physics.box2d.Joint as __Joint
__Joint = __Joint
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RevoluteJoint():
    """com.badlogic.gdx.physics.box2d.joints.RevoluteJoint"""
 
    @staticmethod
    def __wrap(java_value: __RevoluteJoint) -> 'RevoluteJoint':
        return RevoluteJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RevoluteJoint):
        """
        Dynamic initializer for RevoluteJoint.
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
    def enableMotor(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.enableMotor(boolean)"""
        super(__RevoluteJoint, self).enableMotor(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getUpperLimit(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getUpperLimit()"""
        return float.__wrap(super(RevoluteJoint, self).getUpperLimit())

    @overload
    def getMaxMotorTorque(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getMaxMotorTorque()"""
        return float.__wrap(super(RevoluteJoint, self).getMaxMotorTorque())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getMotorSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getMotorSpeed()"""
        return float.__wrap(super(RevoluteJoint, self).getMotorSpeed())

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getLocalAnchorB()"""
        return 'math.Vector2'.__wrap(super(RevoluteJoint, self).getLocalAnchorB())

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorA())

    @overload
    def getMotorTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getMotorTorque(float)"""
        return float.__wrap(super(__RevoluteJoint, self).getMotorTorque(__float.valueOf(arg0)))

    @overload
    def enableLimit(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.enableLimit(boolean)"""
        super(__RevoluteJoint, self).enableLimit(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool.__wrap(super(box2d.Joint, self).getCollideConnected())

    @overload
    def getReferenceAngle(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getReferenceAngle()"""
        return float.__wrap(super(RevoluteJoint, self).getReferenceAngle())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(__box2d.Joint, self).setUserData(arg0)

    @overload
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getLocalAnchorA()"""
        return 'math.Vector2'.__wrap(super(RevoluteJoint, self).getLocalAnchorA())

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object.__wrap(super(box2d.Joint, self).getUserData())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getJointAngle(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getJointAngle()"""
        return float.__wrap(super(RevoluteJoint, self).getJointAngle())

    @overload
    def setMotorSpeed(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.setMotorSpeed(float)"""
        super(__RevoluteJoint, self).setMotorSpeed(__float.valueOf(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'.__wrap(super(box2d.Joint, self).getType())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.RevoluteJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = __RevoluteJoint(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getJointSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getJointSpeed()"""
        return float.__wrap(super(RevoluteJoint, self).getJointSpeed())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'.__wrap(super(__box2d.Joint, self).getReactionForce(__float.valueOf(arg0)))

    @overload
    def setLimits(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.setLimits(float,float)"""
        super(__RevoluteJoint, self).setLimits(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isLimitEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.isLimitEnabled()"""
        return bool.__wrap(super(RevoluteJoint, self).isLimitEnabled())

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float.__wrap(super(__box2d.Joint, self).getReactionTorque(__float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool.__wrap(super(box2d.Joint, self).isActive())

    @overload
    def isMotorEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.isMotorEnabled()"""
        return bool.__wrap(super(RevoluteJoint, self).isMotorEnabled())

    @overload
    def getLowerLimit(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getLowerLimit()"""
        return float.__wrap(super(RevoluteJoint, self).getLowerLimit())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setMaxMotorTorque(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.setMaxMotorTorque(float)"""
        super(__RevoluteJoint, self).setMaxMotorTorque(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.WeldJointDef
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.physics.box2d.joints.WeldJointDef as __WeldJointDef
__WeldJointDef = __WeldJointDef
from builtins import int
 
class WeldJointDef():
    """com.badlogic.gdx.physics.box2d.joints.WeldJointDef"""
 
    @staticmethod
    def __wrap(java_value: __WeldJointDef) -> 'WeldJointDef':
        return WeldJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WeldJointDef):
        """
        Dynamic initializer for WeldJointDef.
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
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.WeldJointDef()"""
        val = __WeldJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.WeldJointDef()"""
        val = __WeldJointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
    def initialize(self, arg0: 'Body', arg1: 'Body', arg2: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.WeldJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2)"""
        super(__WeldJointDef, self).initialize(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.RopeJoint
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef_JointType
__JointType = __JointDef_JointType.JointType
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
from builtins import object
import com.badlogic.gdx.physics.box2d.joints.RopeJoint as __RopeJoint
__RopeJoint = __RopeJoint
import com.badlogic.gdx.physics.box2d.Joint as __Joint
__Joint = __Joint
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RopeJoint():
    """com.badlogic.gdx.physics.box2d.joints.RopeJoint"""
 
    @staticmethod
    def __wrap(java_value: __RopeJoint) -> 'RopeJoint':
        return RopeJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RopeJoint):
        """
        Dynamic initializer for RopeJoint.
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
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.RopeJoint.getLocalAnchorA()"""
        return 'math.Vector2'.__wrap(super(RopeJoint, self).getLocalAnchorA())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool.__wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(__box2d.Joint, self).setUserData(arg0)

    @overload
    def getMaxLength(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RopeJoint.getMaxLength()"""
        return float.__wrap(super(RopeJoint, self).getMaxLength())

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object.__wrap(super(box2d.Joint, self).getUserData())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'.__wrap(super(box2d.Joint, self).getType())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'.__wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.RopeJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = __RopeJoint(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'.__wrap(super(__box2d.Joint, self).getReactionForce(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float.__wrap(super(__box2d.Joint, self).getReactionTorque(__float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'.__wrap(super(box2d.Joint, self).getAnchorB())

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.RopeJoint.getLocalAnchorB()"""
        return 'math.Vector2'.__wrap(super(RopeJoint, self).getLocalAnchorB())

    @overload
    def setMaxLength(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.RopeJoint.setMaxLength(float)"""
        super(__RopeJoint, self).setMaxLength(__float.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool.__wrap(super(box2d.Joint, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()