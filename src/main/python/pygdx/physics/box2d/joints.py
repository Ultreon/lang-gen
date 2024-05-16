from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.joints.RopeJointDef as _RopeJointDef
_RopeJointDef = _RopeJointDef
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RopeJointDef():
    """com.badlogic.gdx.physics.box2d.joints.RopeJointDef"""
 
    @staticmethod
    def _wrap(java_value: _RopeJointDef) -> 'RopeJointDef':
        return RopeJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RopeJointDef):
        """
        Dynamic initializer for RopeJointDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RopeJointDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RopeJointDef__wrapper":
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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.RopeJointDef()"""
        val = _RopeJointDef()
        self.__wrapper = val

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.RopeJointDef()"""
        val = _RopeJointDef()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.RopeJointDef
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.joints.RopeJointDef as _RopeJointDef
_RopeJointDef = _RopeJointDef
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RopeJointDef():
    """com.badlogic.gdx.physics.box2d.joints.RopeJointDef"""
 
    @staticmethod
    def _wrap(java_value: _RopeJointDef) -> 'RopeJointDef':
        return RopeJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RopeJointDef):
        """
        Dynamic initializer for RopeJointDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RopeJointDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RopeJointDef__wrapper":
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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.RopeJointDef()"""
        val = _RopeJointDef()
        self.__wrapper = val

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.RopeJointDef()"""
        val = _RopeJointDef()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.RopeJointDef 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.PrismaticJoint
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.physics.box2d.Joint as _Joint
_Joint = _Joint
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import java.lang.Float as _float
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef_JointType
_JointType = _JointDef_JointType.JointType
import java.lang.Boolean as _boolean
import com.badlogic.gdx.physics.box2d.joints.PrismaticJoint as _PrismaticJoint
_PrismaticJoint = _PrismaticJoint
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PrismaticJoint():
    """com.badlogic.gdx.physics.box2d.joints.PrismaticJoint"""
 
    @staticmethod
    def _wrap(java_value: _PrismaticJoint) -> 'PrismaticJoint':
        return PrismaticJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PrismaticJoint):
        """
        Dynamic initializer for PrismaticJoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PrismaticJoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PrismaticJoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isMotorEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.isMotorEnabled()"""
        return bool._wrap(super(PrismaticJoint, self).isMotorEnabled())

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyB())

    @overload
    def enableMotor(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.enableMotor(boolean)"""
        super(_PrismaticJoint, self).enableMotor(_boolean.valueOf(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'._wrap(super(box2d.Joint, self).getType())

    @overload
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getLocalAnchorA()"""
        return 'math.Vector2'._wrap(super(PrismaticJoint, self).getLocalAnchorA())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLimits(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.setLimits(float,float)"""
        super(_PrismaticJoint, self).setLimits(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getJointTranslation(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getJointTranslation()"""
        return float._wrap(super(PrismaticJoint, self).getJointTranslation())

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float._wrap(super(_box2d.Joint, self).getReactionTorque(_float.valueOf(arg0)))

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'._wrap(super(_box2d.Joint, self).getReactionForce(_float.valueOf(arg0)))

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
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(_box2d.Joint, self).setUserData(arg0)

    @overload
    def setMotorSpeed(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.setMotorSpeed(float)"""
        super(_PrismaticJoint, self).setMotorSpeed(_float.valueOf(arg0))

    @overload
    def getJointSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getJointSpeed()"""
        return float._wrap(super(PrismaticJoint, self).getJointSpeed())

    @overload
    def getLowerLimit(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getLowerLimit()"""
        return float._wrap(super(PrismaticJoint, self).getLowerLimit())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.PrismaticJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = _PrismaticJoint(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @overload
    def getReferenceAngle(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getReferenceAngle()"""
        return float._wrap(super(PrismaticJoint, self).getReferenceAngle())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getMaxMotorForce(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getMaxMotorForce()"""
        return float._wrap(super(PrismaticJoint, self).getMaxMotorForce())

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyA())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object._wrap(super(box2d.Joint, self).getUserData())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getMotorForce(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getMotorForce(float)"""
        return float._wrap(super(_PrismaticJoint, self).getMotorForce(_float.valueOf(arg0)))

    @overload
    def getMotorSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getMotorSpeed()"""
        return float._wrap(super(PrismaticJoint, self).getMotorSpeed())

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getLocalAnchorB()"""
        return 'math.Vector2'._wrap(super(PrismaticJoint, self).getLocalAnchorB())

    @overload
    def getLocalAxisA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getLocalAxisA()"""
        return 'math.Vector2'._wrap(super(PrismaticJoint, self).getLocalAxisA())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool._wrap(super(box2d.Joint, self).isActive())

    @overload
    def isLimitEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.isLimitEnabled()"""
        return bool._wrap(super(PrismaticJoint, self).isLimitEnabled())

    @overload
    def setMaxMotorForce(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.setMaxMotorForce(float)"""
        super(_PrismaticJoint, self).setMaxMotorForce(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def enableLimit(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.enableLimit(boolean)"""
        super(_PrismaticJoint, self).enableLimit(_boolean.valueOf(arg0))

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool._wrap(super(box2d.Joint, self).getCollideConnected())

    @overload
    def getUpperLimit(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PrismaticJoint.getUpperLimit()"""
        return float._wrap(super(PrismaticJoint, self).getUpperLimit())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.MotorJointDef
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.physics.box2d.joints.MotorJointDef as _MotorJointDef
_MotorJointDef = _MotorJointDef
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MotorJointDef():
    """com.badlogic.gdx.physics.box2d.joints.MotorJointDef"""
 
    @staticmethod
    def _wrap(java_value: _MotorJointDef) -> 'MotorJointDef':
        return MotorJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MotorJointDef):
        """
        Dynamic initializer for MotorJointDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MotorJointDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MotorJointDef__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def initialize(self, arg0: 'Body', arg1: 'Body'):
        """public void com.badlogic.gdx.physics.box2d.joints.MotorJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body)"""
        super(_MotorJointDef, self).initialize(arg0, arg1)

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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.MotorJointDef()"""
        val = _MotorJointDef()
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.MotorJointDef()"""
        val = _MotorJointDef()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.GearJoint
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.physics.box2d.joints.GearJoint as _GearJoint
_GearJoint = _GearJoint
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.physics.box2d.Joint as _Joint
_Joint = _Joint
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import java.lang.Float as _float
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef_JointType
_JointType = _JointDef_JointType.JointType
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GearJoint():
    """com.badlogic.gdx.physics.box2d.joints.GearJoint"""
 
    @staticmethod
    def _wrap(java_value: _GearJoint) -> 'GearJoint':
        return GearJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GearJoint):
        """
        Dynamic initializer for GearJoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GearJoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GearJoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'._wrap(super(box2d.Joint, self).getType())

    @overload
    def getJoint2(self) -> 'box2d.Joint':
        """public com.badlogic.gdx.physics.box2d.Joint com.badlogic.gdx.physics.box2d.joints.GearJoint.getJoint2()"""
        return 'box2d.Joint'._wrap(super(GearJoint, self).getJoint2())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'World', arg1: int, arg2: 'Joint', arg3: 'Joint'):
        """public com.badlogic.gdx.physics.box2d.joints.GearJoint(com.badlogic.gdx.physics.box2d.World,long,com.badlogic.gdx.physics.box2d.Joint,com.badlogic.gdx.physics.box2d.Joint)"""
        val = _GearJoint(arg0, _long.valueOf(arg1), arg2, arg3)
        self.__wrapper = val

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float._wrap(super(_box2d.Joint, self).getReactionTorque(_float.valueOf(arg0)))

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'._wrap(super(_box2d.Joint, self).getReactionForce(_float.valueOf(arg0)))

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
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(_box2d.Joint, self).setUserData(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def getJoint1(self) -> 'box2d.Joint':
        """public com.badlogic.gdx.physics.box2d.Joint com.badlogic.gdx.physics.box2d.joints.GearJoint.getJoint1()"""
        return 'box2d.Joint'._wrap(super(GearJoint, self).getJoint1())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object._wrap(super(box2d.Joint, self).getUserData())

    @overload
    def getRatio(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.GearJoint.getRatio()"""
        return float._wrap(super(GearJoint, self).getRatio())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorB())

    @overload
    def setRatio(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.GearJoint.setRatio(float)"""
        super(_GearJoint, self).setRatio(_float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool._wrap(super(box2d.Joint, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool._wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.FrictionJoint
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.physics.box2d.Joint as _Joint
_Joint = _Joint
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import java.lang.Float as _float
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef_JointType
_JointType = _JointDef_JointType.JointType
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.joints.FrictionJoint as _FrictionJoint
_FrictionJoint = _FrictionJoint
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FrictionJoint():
    """com.badlogic.gdx.physics.box2d.joints.FrictionJoint"""
 
    @staticmethod
    def _wrap(java_value: _FrictionJoint) -> 'FrictionJoint':
        return FrictionJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FrictionJoint):
        """
        Dynamic initializer for FrictionJoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FrictionJoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FrictionJoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyB())

    @overload
    def getMaxForce(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.FrictionJoint.getMaxForce()"""
        return float._wrap(super(FrictionJoint, self).getMaxForce())

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'._wrap(super(box2d.Joint, self).getType())

    @overload
    def setMaxForce(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.FrictionJoint.setMaxForce(float)"""
        super(_FrictionJoint, self).setMaxForce(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float._wrap(super(_box2d.Joint, self).getReactionTorque(_float.valueOf(arg0)))

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'._wrap(super(_box2d.Joint, self).getReactionForce(_float.valueOf(arg0)))

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
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(_box2d.Joint, self).setUserData(arg0)

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.FrictionJoint.getLocalAnchorB()"""
        return 'math.Vector2'._wrap(super(FrictionJoint, self).getLocalAnchorB())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def getMaxTorque(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.FrictionJoint.getMaxTorque()"""
        return float._wrap(super(FrictionJoint, self).getMaxTorque())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.FrictionJoint.getLocalAnchorA()"""
        return 'math.Vector2'._wrap(super(FrictionJoint, self).getLocalAnchorA())

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object._wrap(super(box2d.Joint, self).getUserData())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setMaxTorque(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.FrictionJoint.setMaxTorque(float)"""
        super(_FrictionJoint, self).setMaxTorque(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.FrictionJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = _FrictionJoint(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool._wrap(super(box2d.Joint, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool._wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.PulleyJointDef
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.joints.PulleyJointDef as _PulleyJointDef
_PulleyJointDef = _PulleyJointDef
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PulleyJointDef():
    """com.badlogic.gdx.physics.box2d.joints.PulleyJointDef"""
 
    @staticmethod
    def _wrap(java_value: _PulleyJointDef) -> 'PulleyJointDef':
        return PulleyJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PulleyJointDef):
        """
        Dynamic initializer for PulleyJointDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PulleyJointDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PulleyJointDef__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def initialize(self, arg0: 'Body', arg1: 'Body', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2', arg5: 'Vector2', arg6: float):
        """public void com.badlogic.gdx.physics.box2d.joints.PulleyJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        super(_PulleyJointDef, self).initialize(arg0, arg1, arg2, arg3, arg4, arg5, _float.valueOf(arg6))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.PulleyJointDef()"""
        val = _PulleyJointDef()
        self.__wrapper = val

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.PulleyJointDef()"""
        val = _PulleyJointDef()
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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.RevoluteJointDef
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.joints.RevoluteJointDef as _RevoluteJointDef
_RevoluteJointDef = _RevoluteJointDef
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RevoluteJointDef():
    """com.badlogic.gdx.physics.box2d.joints.RevoluteJointDef"""
 
    @staticmethod
    def _wrap(java_value: _RevoluteJointDef) -> 'RevoluteJointDef':
        return RevoluteJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RevoluteJointDef):
        """
        Dynamic initializer for RevoluteJointDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RevoluteJointDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RevoluteJointDef__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.RevoluteJointDef()"""
        val = _RevoluteJointDef()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.RevoluteJointDef()"""
        val = _RevoluteJointDef()
        self.__wrapper = val

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def initialize(self, arg0: 'Body', arg1: 'Body', arg2: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.RevoluteJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2)"""
        super(_RevoluteJointDef, self).initialize(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.MouseJoint
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.physics.box2d.Joint as _Joint
_Joint = _Joint
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import java.lang.Float as _float
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef_JointType
_JointType = _JointDef_JointType.JointType
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.joints.MouseJoint as _MouseJoint
_MouseJoint = _MouseJoint
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MouseJoint():
    """com.badlogic.gdx.physics.box2d.joints.MouseJoint"""
 
    @staticmethod
    def _wrap(java_value: _MouseJoint) -> 'MouseJoint':
        return MouseJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MouseJoint):
        """
        Dynamic initializer for MouseJoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MouseJoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MouseJoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyB())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.MouseJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = _MouseJoint(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @overload
    def setMaxForce(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MouseJoint.setMaxForce(float)"""
        super(_MouseJoint, self).setMaxForce(_float.valueOf(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'._wrap(super(box2d.Joint, self).getType())

    @overload
    def getDampingRatio(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MouseJoint.getDampingRatio()"""
        return float._wrap(super(MouseJoint, self).getDampingRatio())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getMaxForce(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MouseJoint.getMaxForce()"""
        return float._wrap(super(MouseJoint, self).getMaxForce())

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float._wrap(super(_box2d.Joint, self).getReactionTorque(_float.valueOf(arg0)))

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'._wrap(super(_box2d.Joint, self).getReactionForce(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setFrequency(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MouseJoint.setFrequency(float)"""
        super(_MouseJoint, self).setFrequency(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setDampingRatio(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MouseJoint.setDampingRatio(float)"""
        super(_MouseJoint, self).setDampingRatio(_float.valueOf(arg0))

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(_box2d.Joint, self).setUserData(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def getTarget(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.MouseJoint.getTarget()"""
        return 'math.Vector2'._wrap(super(MouseJoint, self).getTarget())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object._wrap(super(box2d.Joint, self).getUserData())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getFrequency(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MouseJoint.getFrequency()"""
        return float._wrap(super(MouseJoint, self).getFrequency())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool._wrap(super(box2d.Joint, self).isActive())

    @overload
    def setTarget(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.MouseJoint.setTarget(com.badlogic.gdx.math.Vector2)"""
        super(_MouseJoint, self).setTarget(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool._wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.DistanceJointDef
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.joints.DistanceJointDef as _DistanceJointDef
_DistanceJointDef = _DistanceJointDef
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DistanceJointDef():
    """com.badlogic.gdx.physics.box2d.joints.DistanceJointDef"""
 
    @staticmethod
    def _wrap(java_value: _DistanceJointDef) -> 'DistanceJointDef':
        return DistanceJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DistanceJointDef):
        """
        Dynamic initializer for DistanceJointDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DistanceJointDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DistanceJointDef__wrapper":
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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.DistanceJointDef()"""
        val = _DistanceJointDef()
        self.__wrapper = val

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def initialize(self, arg0: 'Body', arg1: 'Body', arg2: 'Vector2', arg3: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.DistanceJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_DistanceJointDef, self).initialize(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.DistanceJointDef()"""
        val = _DistanceJointDef()
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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.RopeJoint
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.physics.box2d.Joint as _Joint
_Joint = _Joint
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import com.badlogic.gdx.physics.box2d.joints.RopeJoint as _RopeJoint
_RopeJoint = _RopeJoint
import java.lang.Float as _float
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef_JointType
_JointType = _JointDef_JointType.JointType
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RopeJoint():
    """com.badlogic.gdx.physics.box2d.joints.RopeJoint"""
 
    @staticmethod
    def _wrap(java_value: _RopeJoint) -> 'RopeJoint':
        return RopeJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RopeJoint):
        """
        Dynamic initializer for RopeJoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RopeJoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RopeJoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'._wrap(super(box2d.Joint, self).getType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.RopeJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = _RopeJoint(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float._wrap(super(_box2d.Joint, self).getReactionTorque(_float.valueOf(arg0)))

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'._wrap(super(_box2d.Joint, self).getReactionForce(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.RopeJoint.getLocalAnchorA()"""
        return 'math.Vector2'._wrap(super(RopeJoint, self).getLocalAnchorA())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(_box2d.Joint, self).setUserData(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setMaxLength(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.RopeJoint.setMaxLength(float)"""
        super(_RopeJoint, self).setMaxLength(_float.valueOf(arg0))

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def getMaxLength(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RopeJoint.getMaxLength()"""
        return float._wrap(super(RopeJoint, self).getMaxLength())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object._wrap(super(box2d.Joint, self).getUserData())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorB())

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.RopeJoint.getLocalAnchorB()"""
        return 'math.Vector2'._wrap(super(RopeJoint, self).getLocalAnchorB())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool._wrap(super(box2d.Joint, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool._wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.GearJointDef
from builtins import str
import com.badlogic.gdx.physics.box2d.joints.GearJointDef as _GearJointDef
_GearJointDef = _GearJointDef
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GearJointDef():
    """com.badlogic.gdx.physics.box2d.joints.GearJointDef"""
 
    @staticmethod
    def _wrap(java_value: _GearJointDef) -> 'GearJointDef':
        return GearJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GearJointDef):
        """
        Dynamic initializer for GearJointDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GearJointDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GearJointDef__wrapper":
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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.GearJointDef()"""
        val = _GearJointDef()
        self.__wrapper = val

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
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.GearJointDef()"""
        val = _GearJointDef()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.MotorJoint
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.physics.box2d.Joint as _Joint
_Joint = _Joint
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import java.lang.Float as _float
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef_JointType
_JointType = _JointDef_JointType.JointType
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.physics.box2d.joints.MotorJoint as _MotorJoint
_MotorJoint = _MotorJoint
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MotorJoint():
    """com.badlogic.gdx.physics.box2d.joints.MotorJoint"""
 
    @staticmethod
    def _wrap(java_value: _MotorJoint) -> 'MotorJoint':
        return MotorJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MotorJoint):
        """
        Dynamic initializer for MotorJoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MotorJoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MotorJoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyB())

    @overload
    def setCorrectionFactor(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MotorJoint.setCorrectionFactor(float)"""
        super(_MotorJoint, self).setCorrectionFactor(_float.valueOf(arg0))

    @overload
    def getMaxForce(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MotorJoint.getMaxForce()"""
        return float._wrap(super(MotorJoint, self).getMaxForce())

    @overload
    def getAngularOffset(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MotorJoint.getAngularOffset()"""
        return float._wrap(super(MotorJoint, self).getAngularOffset())

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'._wrap(super(box2d.Joint, self).getType())

    @overload
    def getCorrectionFactor(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MotorJoint.getCorrectionFactor()"""
        return float._wrap(super(MotorJoint, self).getCorrectionFactor())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.MotorJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = _MotorJoint(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getLinearOffset(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.MotorJoint.getLinearOffset()"""
        return 'math.Vector2'._wrap(super(MotorJoint, self).getLinearOffset())

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float._wrap(super(_box2d.Joint, self).getReactionTorque(_float.valueOf(arg0)))

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'._wrap(super(_box2d.Joint, self).getReactionForce(_float.valueOf(arg0)))

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
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(_box2d.Joint, self).setUserData(arg0)

    @overload
    def setAngularOffset(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MotorJoint.setAngularOffset(float)"""
        super(_MotorJoint, self).setAngularOffset(_float.valueOf(arg0))

    @overload
    def getMaxTorque(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.MotorJoint.getMaxTorque()"""
        return float._wrap(super(MotorJoint, self).getMaxTorque())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def setMaxForce(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MotorJoint.setMaxForce(float)"""
        super(_MotorJoint, self).setMaxForce(_float.valueOf(arg0))

    @overload
    def setLinearOffset(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.MotorJoint.setLinearOffset(com.badlogic.gdx.math.Vector2)"""
        super(_MotorJoint, self).setLinearOffset(arg0)

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object._wrap(super(box2d.Joint, self).getUserData())

    @overload
    def setMaxTorque(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.MotorJoint.setMaxTorque(float)"""
        super(_MotorJoint, self).setMaxTorque(_float.valueOf(arg0))

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool._wrap(super(box2d.Joint, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool._wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.DistanceJoint
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.physics.box2d.Joint as _Joint
_Joint = _Joint
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.physics.box2d.joints.DistanceJoint as _DistanceJoint
_DistanceJoint = _DistanceJoint
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import java.lang.Float as _float
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef_JointType
_JointType = _JointDef_JointType.JointType
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DistanceJoint():
    """com.badlogic.gdx.physics.box2d.joints.DistanceJoint"""
 
    @staticmethod
    def _wrap(java_value: _DistanceJoint) -> 'DistanceJoint':
        return DistanceJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DistanceJoint):
        """
        Dynamic initializer for DistanceJoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DistanceJoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DistanceJoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'._wrap(super(box2d.Joint, self).getType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLength(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.DistanceJoint.setLength(float)"""
        super(_DistanceJoint, self).setLength(_float.valueOf(arg0))

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float._wrap(super(_box2d.Joint, self).getReactionTorque(_float.valueOf(arg0)))

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'._wrap(super(_box2d.Joint, self).getReactionForce(_float.valueOf(arg0)))

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
    def getLength(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.DistanceJoint.getLength()"""
        return float._wrap(super(DistanceJoint, self).getLength())

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(_box2d.Joint, self).setUserData(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.DistanceJoint.getLocalAnchorB()"""
        return 'math.Vector2'._wrap(super(DistanceJoint, self).getLocalAnchorB())

    @overload
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.DistanceJoint.getLocalAnchorA()"""
        return 'math.Vector2'._wrap(super(DistanceJoint, self).getLocalAnchorA())

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyA())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getDampingRatio(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.DistanceJoint.getDampingRatio()"""
        return float._wrap(super(DistanceJoint, self).getDampingRatio())

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object._wrap(super(box2d.Joint, self).getUserData())

    @overload
    def setFrequency(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.DistanceJoint.setFrequency(float)"""
        super(_DistanceJoint, self).setFrequency(_float.valueOf(arg0))

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.DistanceJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = _DistanceJoint(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @overload
    def setDampingRatio(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.DistanceJoint.setDampingRatio(float)"""
        super(_DistanceJoint, self).setDampingRatio(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool._wrap(super(box2d.Joint, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool._wrap(super(box2d.Joint, self).getCollideConnected())

    @overload
    def getFrequency(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.DistanceJoint.getFrequency()"""
        return float._wrap(super(DistanceJoint, self).getFrequency())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.WeldJointDef
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.joints.WeldJointDef as _WeldJointDef
_WeldJointDef = _WeldJointDef
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WeldJointDef():
    """com.badlogic.gdx.physics.box2d.joints.WeldJointDef"""
 
    @staticmethod
    def _wrap(java_value: _WeldJointDef) -> 'WeldJointDef':
        return WeldJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WeldJointDef):
        """
        Dynamic initializer for WeldJointDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WeldJointDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WeldJointDef__wrapper":
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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.WeldJointDef()"""
        val = _WeldJointDef()
        self.__wrapper = val

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
    def initialize(self, arg0: 'Body', arg1: 'Body', arg2: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.WeldJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2)"""
        super(_WeldJointDef, self).initialize(arg0, arg1, arg2)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.WeldJointDef()"""
        val = _WeldJointDef()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.PrismaticJointDef
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.physics.box2d.joints.PrismaticJointDef as _PrismaticJointDef
_PrismaticJointDef = _PrismaticJointDef
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PrismaticJointDef():
    """com.badlogic.gdx.physics.box2d.joints.PrismaticJointDef"""
 
    @staticmethod
    def _wrap(java_value: _PrismaticJointDef) -> 'PrismaticJointDef':
        return PrismaticJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PrismaticJointDef):
        """
        Dynamic initializer for PrismaticJointDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PrismaticJointDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PrismaticJointDef__wrapper":
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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.PrismaticJointDef()"""
        val = _PrismaticJointDef()
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
        """public void com.badlogic.gdx.physics.box2d.joints.PrismaticJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_PrismaticJointDef, self).initialize(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.PrismaticJointDef()"""
        val = _PrismaticJointDef()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.FrictionJointDef
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.joints.FrictionJointDef as _FrictionJointDef
_FrictionJointDef = _FrictionJointDef
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FrictionJointDef():
    """com.badlogic.gdx.physics.box2d.joints.FrictionJointDef"""
 
    @staticmethod
    def _wrap(java_value: _FrictionJointDef) -> 'FrictionJointDef':
        return FrictionJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FrictionJointDef):
        """
        Dynamic initializer for FrictionJointDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FrictionJointDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FrictionJointDef__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def initialize(self, arg0: 'Body', arg1: 'Body', arg2: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.FrictionJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2)"""
        super(_FrictionJointDef, self).initialize(arg0, arg1, arg2)

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
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.FrictionJointDef()"""
        val = _FrictionJointDef()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.FrictionJointDef()"""
        val = _FrictionJointDef()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.RevoluteJoint
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.physics.box2d.Joint as _Joint
_Joint = _Joint
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.joints.RevoluteJoint as _RevoluteJoint
_RevoluteJoint = _RevoluteJoint
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import java.lang.Float as _float
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef_JointType
_JointType = _JointDef_JointType.JointType
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RevoluteJoint():
    """com.badlogic.gdx.physics.box2d.joints.RevoluteJoint"""
 
    @staticmethod
    def _wrap(java_value: _RevoluteJoint) -> 'RevoluteJoint':
        return RevoluteJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RevoluteJoint):
        """
        Dynamic initializer for RevoluteJoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RevoluteJoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RevoluteJoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isLimitEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.isLimitEnabled()"""
        return bool._wrap(super(RevoluteJoint, self).isLimitEnabled())

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyB())

    @overload
    def setLimits(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.setLimits(float,float)"""
        super(_RevoluteJoint, self).setLimits(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'._wrap(super(box2d.Joint, self).getType())

    @overload
    def isMotorEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.isMotorEnabled()"""
        return bool._wrap(super(RevoluteJoint, self).isMotorEnabled())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.RevoluteJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = _RevoluteJoint(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @overload
    def setMotorSpeed(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.setMotorSpeed(float)"""
        super(_RevoluteJoint, self).setMotorSpeed(_float.valueOf(arg0))

    @overload
    def getUpperLimit(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getUpperLimit()"""
        return float._wrap(super(RevoluteJoint, self).getUpperLimit())

    @overload
    def getReferenceAngle(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getReferenceAngle()"""
        return float._wrap(super(RevoluteJoint, self).getReferenceAngle())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getLocalAnchorB()"""
        return 'math.Vector2'._wrap(super(RevoluteJoint, self).getLocalAnchorB())

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float._wrap(super(_box2d.Joint, self).getReactionTorque(_float.valueOf(arg0)))

    @overload
    def setMaxMotorTorque(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.setMaxMotorTorque(float)"""
        super(_RevoluteJoint, self).setMaxMotorTorque(_float.valueOf(arg0))

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'._wrap(super(_box2d.Joint, self).getReactionForce(_float.valueOf(arg0)))

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
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(_box2d.Joint, self).setUserData(arg0)

    @overload
    def getMaxMotorTorque(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getMaxMotorTorque()"""
        return float._wrap(super(RevoluteJoint, self).getMaxMotorTorque())

    @overload
    def enableMotor(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.enableMotor(boolean)"""
        super(_RevoluteJoint, self).enableMotor(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyA())

    @overload
    def getJointAngle(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getJointAngle()"""
        return float._wrap(super(RevoluteJoint, self).getJointAngle())

    @overload
    def getMotorTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getMotorTorque(float)"""
        return float._wrap(super(_RevoluteJoint, self).getMotorTorque(_float.valueOf(arg0)))

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object._wrap(super(box2d.Joint, self).getUserData())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getJointSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getJointSpeed()"""
        return float._wrap(super(RevoluteJoint, self).getJointSpeed())

    @overload
    def getLowerLimit(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getLowerLimit()"""
        return float._wrap(super(RevoluteJoint, self).getLowerLimit())

    @overload
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getLocalAnchorA()"""
        return 'math.Vector2'._wrap(super(RevoluteJoint, self).getLocalAnchorA())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool._wrap(super(box2d.Joint, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getMotorSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.getMotorSpeed()"""
        return float._wrap(super(RevoluteJoint, self).getMotorSpeed())

    @overload
    def enableLimit(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.joints.RevoluteJoint.enableLimit(boolean)"""
        super(_RevoluteJoint, self).enableLimit(_boolean.valueOf(arg0))

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool._wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.PulleyJoint
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.physics.box2d.Joint as _Joint
_Joint = _Joint
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import java.lang.Float as _float
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef_JointType
_JointType = _JointDef_JointType.JointType
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.physics.box2d.joints.PulleyJoint as _PulleyJoint
_PulleyJoint = _PulleyJoint
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PulleyJoint():
    """com.badlogic.gdx.physics.box2d.joints.PulleyJoint"""
 
    @staticmethod
    def _wrap(java_value: _PulleyJoint) -> 'PulleyJoint':
        return PulleyJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PulleyJoint):
        """
        Dynamic initializer for PulleyJoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PulleyJoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PulleyJoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyB())

    @overload
    def getLength2(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PulleyJoint.getLength2()"""
        return float._wrap(super(PulleyJoint, self).getLength2())

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'._wrap(super(box2d.Joint, self).getType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.PulleyJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = _PulleyJoint(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @overload
    def getGroundAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.PulleyJoint.getGroundAnchorA()"""
        return 'math.Vector2'._wrap(super(PulleyJoint, self).getGroundAnchorA())

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float._wrap(super(_box2d.Joint, self).getReactionTorque(_float.valueOf(arg0)))

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'._wrap(super(_box2d.Joint, self).getReactionForce(_float.valueOf(arg0)))

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
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(_box2d.Joint, self).setUserData(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyA())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object._wrap(super(box2d.Joint, self).getUserData())

    @overload
    def getLength1(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PulleyJoint.getLength1()"""
        return float._wrap(super(PulleyJoint, self).getLength1())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorB())

    @overload
    def getRatio(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.PulleyJoint.getRatio()"""
        return float._wrap(super(PulleyJoint, self).getRatio())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getGroundAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.PulleyJoint.getGroundAnchorB()"""
        return 'math.Vector2'._wrap(super(PulleyJoint, self).getGroundAnchorB())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool._wrap(super(box2d.Joint, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool._wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.MouseJointDef
import com.badlogic.gdx.physics.box2d.joints.MouseJointDef as _MouseJointDef
_MouseJointDef = _MouseJointDef
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MouseJointDef():
    """com.badlogic.gdx.physics.box2d.joints.MouseJointDef"""
 
    @staticmethod
    def _wrap(java_value: _MouseJointDef) -> 'MouseJointDef':
        return MouseJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MouseJointDef):
        """
        Dynamic initializer for MouseJointDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MouseJointDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MouseJointDef__wrapper":
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.MouseJointDef()"""
        val = _MouseJointDef()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.MouseJointDef()"""
        val = _MouseJointDef()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.WheelJoint
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.physics.box2d.Joint as _Joint
_Joint = _Joint
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import java.lang.Float as _float
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef_JointType
_JointType = _JointDef_JointType.JointType
import com.badlogic.gdx.physics.box2d.joints.WheelJoint as _WheelJoint
_WheelJoint = _WheelJoint
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WheelJoint():
    """com.badlogic.gdx.physics.box2d.joints.WheelJoint"""
 
    @staticmethod
    def _wrap(java_value: _WheelJoint) -> 'WheelJoint':
        return WheelJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WheelJoint):
        """
        Dynamic initializer for WheelJoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WheelJoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WheelJoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setMotorSpeed(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.WheelJoint.setMotorSpeed(float)"""
        super(_WheelJoint, self).setMotorSpeed(_float.valueOf(arg0))

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyB())

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'._wrap(super(box2d.Joint, self).getType())

    @overload
    def getMotorSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getMotorSpeed()"""
        return float._wrap(super(WheelJoint, self).getMotorSpeed())

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.WheelJoint.getLocalAnchorB()"""
        return 'math.Vector2'._wrap(super(WheelJoint, self).getLocalAnchorB())

    @overload
    def getSpringDampingRatio(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getSpringDampingRatio()"""
        return float._wrap(super(WheelJoint, self).getSpringDampingRatio())

    @overload
    def getSpringFrequencyHz(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getSpringFrequencyHz()"""
        return float._wrap(super(WheelJoint, self).getSpringFrequencyHz())

    @overload
    def isMotorEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.joints.WheelJoint.isMotorEnabled()"""
        return bool._wrap(super(WheelJoint, self).isMotorEnabled())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float._wrap(super(_box2d.Joint, self).getReactionTorque(_float.valueOf(arg0)))

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'._wrap(super(_box2d.Joint, self).getReactionForce(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setSpringFrequencyHz(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.WheelJoint.setSpringFrequencyHz(float)"""
        super(_WheelJoint, self).setSpringFrequencyHz(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.WheelJoint.getLocalAnchorA()"""
        return 'math.Vector2'._wrap(super(WheelJoint, self).getLocalAnchorA())

    @override
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(_box2d.Joint, self).setUserData(arg0)

    @overload
    def getMotorTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getMotorTorque(float)"""
        return float._wrap(super(_WheelJoint, self).getMotorTorque(_float.valueOf(arg0)))

    @overload
    def getJointTranslation(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getJointTranslation()"""
        return float._wrap(super(WheelJoint, self).getJointTranslation())

    @overload
    def enableMotor(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.joints.WheelJoint.enableMotor(boolean)"""
        super(_WheelJoint, self).enableMotor(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setSpringDampingRatio(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.WheelJoint.setSpringDampingRatio(float)"""
        super(_WheelJoint, self).setSpringDampingRatio(_float.valueOf(arg0))

    @overload
    def getMaxMotorTorque(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getMaxMotorTorque()"""
        return float._wrap(super(WheelJoint, self).getMaxMotorTorque())

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyA())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object._wrap(super(box2d.Joint, self).getUserData())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setMaxMotorTorque(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.WheelJoint.setMaxMotorTorque(float)"""
        super(_WheelJoint, self).setMaxMotorTorque(_float.valueOf(arg0))

    @overload
    def getJointSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WheelJoint.getJointSpeed()"""
        return float._wrap(super(WheelJoint, self).getJointSpeed())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.WheelJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = _WheelJoint(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool._wrap(super(box2d.Joint, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getLocalAxisA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.WheelJoint.getLocalAxisA()"""
        return 'math.Vector2'._wrap(super(WheelJoint, self).getLocalAxisA())

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool._wrap(super(box2d.Joint, self).getCollideConnected())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.WheelJointDef
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.physics.box2d.joints.WheelJointDef as _WheelJointDef
_WheelJointDef = _WheelJointDef
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WheelJointDef():
    """com.badlogic.gdx.physics.box2d.joints.WheelJointDef"""
 
    @staticmethod
    def _wrap(java_value: _WheelJointDef) -> 'WheelJointDef':
        return WheelJointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WheelJointDef):
        """
        Dynamic initializer for WheelJointDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WheelJointDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WheelJointDef__wrapper":
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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.joints.WheelJointDef()"""
        val = _WheelJointDef()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def initialize(self, arg0: 'Body', arg1: 'Body', arg2: 'Vector2', arg3: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.joints.WheelJointDef.initialize(com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.physics.box2d.Body,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_WheelJointDef, self).initialize(arg0, arg1, arg2, arg3)

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.joints.WheelJointDef()"""
        val = _WheelJointDef()
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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.joints.WeldJoint
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.physics.box2d.Joint as _Joint
_Joint = _Joint
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import java.lang.Float as _float
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef_JointType
_JointType = _JointDef_JointType.JointType
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.joints.WeldJoint as _WeldJoint
_WeldJoint = _WeldJoint
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WeldJoint():
    """com.badlogic.gdx.physics.box2d.joints.WeldJoint"""
 
    @staticmethod
    def _wrap(java_value: _WeldJoint) -> 'WeldJoint':
        return WeldJoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WeldJoint):
        """
        Dynamic initializer for WeldJoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WeldJoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WeldJoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getLocalAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.WeldJoint.getLocalAnchorA()"""
        return 'math.Vector2'._wrap(super(WeldJoint, self).getLocalAnchorA())

    @override
    @overload
    def getBodyB(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyB())

    @overload
    def setDampingRatio(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.WeldJoint.setDampingRatio(float)"""
        super(_WeldJoint, self).setDampingRatio(_float.valueOf(arg0))

    @override
    @overload
    def getType(self) -> 'box2d.JointDef$JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'box2d.JointDef$JointType'._wrap(super(box2d.Joint, self).getType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float._wrap(super(_box2d.Joint, self).getReactionTorque(_float.valueOf(arg0)))

    @overload
    def getFrequency(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WeldJoint.getFrequency()"""
        return float._wrap(super(WeldJoint, self).getFrequency())

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'._wrap(super(_box2d.Joint, self).getReactionForce(_float.valueOf(arg0)))

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
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(_box2d.Joint, self).setUserData(arg0)

    @overload
    def getReferenceAngle(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WeldJoint.getReferenceAngle()"""
        return float._wrap(super(WeldJoint, self).getReferenceAngle())

    @overload
    def setFrequency(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.joints.WeldJoint.setFrequency(float)"""
        super(_WeldJoint, self).setFrequency(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getBodyA(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'box2d.Body'._wrap(super(box2d.Joint, self).getBodyA())

    @override
    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorA())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object._wrap(super(box2d.Joint, self).getUserData())

    @override
    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'._wrap(super(box2d.Joint, self).getAnchorB())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'World', arg1: int):
        """public com.badlogic.gdx.physics.box2d.joints.WeldJoint(com.badlogic.gdx.physics.box2d.World,long)"""
        val = _WeldJoint(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getDampingRatio(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.joints.WeldJoint.getDampingRatio()"""
        return float._wrap(super(WeldJoint, self).getDampingRatio())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool._wrap(super(box2d.Joint, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool._wrap(super(box2d.Joint, self).getCollideConnected())

    @overload
    def getLocalAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.joints.WeldJoint.getLocalAnchorB()"""
        return 'math.Vector2'._wrap(super(WeldJoint, self).getLocalAnchorB())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())