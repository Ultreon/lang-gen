from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.awt.image.BufferedImage as __BufferedImage
__BufferedImage = __BufferedImage
import com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator as __DistanceFieldGenerator
__DistanceFieldGenerator = __DistanceFieldGenerator
import java.awt.Color as __Color
__Color = __Color
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.awt.Color as Color
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DistanceFieldGenerator():
    """com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator"""
 
    @staticmethod
    def __wrap(java_value: __DistanceFieldGenerator) -> 'DistanceFieldGenerator':
        return DistanceFieldGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DistanceFieldGenerator):
        """
        Dynamic initializer for DistanceFieldGenerator.
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
    def setSpread(self, arg0: float):
        """public void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.setSpread(float)"""
        super(__DistanceFieldGenerator, self).setSpread(__float.valueOf(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator()"""
        val = __DistanceFieldGenerator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getDownscale(self) -> int:
        """public int com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.getDownscale()"""
        return int.__wrap(super(DistanceFieldGenerator, self).getDownscale())

    @overload
    def getSpread(self) -> float:
        """public float com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.getSpread()"""
        return float.__wrap(super(DistanceFieldGenerator, self).getSpread())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setDownscale(self, arg0: int):
        """public void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.setDownscale(int)"""
        super(__DistanceFieldGenerator, self).setDownscale(__int.valueOf(arg0))

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
    def generateDistanceField(self, arg0: 'BufferedImage') -> 'BufferedImage':
        """public java.awt.image.BufferedImage com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.generateDistanceField(java.awt.image.BufferedImage)"""
        return 'BufferedImage'.__wrap(super(__DistanceFieldGenerator, self).generateDistanceField(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator()"""
        val = __DistanceFieldGenerator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.getColor()"""
        return 'Color'.__wrap(super(DistanceFieldGenerator, self).getColor())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.main(java.lang.String[])"""
        __DistanceFieldGenerator.main(arg0)

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.setColor(java.awt.Color)"""
        super(__DistanceFieldGenerator, self).setColor(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.awt.image.BufferedImage as __BufferedImage
__BufferedImage = __BufferedImage
import com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator as __DistanceFieldGenerator
__DistanceFieldGenerator = __DistanceFieldGenerator
import java.awt.Color as __Color
__Color = __Color
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.awt.Color as Color
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DistanceFieldGenerator():
    """com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator"""
 
    @staticmethod
    def __wrap(java_value: __DistanceFieldGenerator) -> 'DistanceFieldGenerator':
        return DistanceFieldGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DistanceFieldGenerator):
        """
        Dynamic initializer for DistanceFieldGenerator.
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
    def setSpread(self, arg0: float):
        """public void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.setSpread(float)"""
        super(__DistanceFieldGenerator, self).setSpread(__float.valueOf(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator()"""
        val = __DistanceFieldGenerator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getDownscale(self) -> int:
        """public int com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.getDownscale()"""
        return int.__wrap(super(DistanceFieldGenerator, self).getDownscale())

    @overload
    def getSpread(self) -> float:
        """public float com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.getSpread()"""
        return float.__wrap(super(DistanceFieldGenerator, self).getSpread())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setDownscale(self, arg0: int):
        """public void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.setDownscale(int)"""
        super(__DistanceFieldGenerator, self).setDownscale(__int.valueOf(arg0))

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
    def generateDistanceField(self, arg0: 'BufferedImage') -> 'BufferedImage':
        """public java.awt.image.BufferedImage com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.generateDistanceField(java.awt.image.BufferedImage)"""
        return 'BufferedImage'.__wrap(super(__DistanceFieldGenerator, self).generateDistanceField(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator()"""
        val = __DistanceFieldGenerator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.getColor()"""
        return 'Color'.__wrap(super(DistanceFieldGenerator, self).getColor())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.main(java.lang.String[])"""
        __DistanceFieldGenerator.main(arg0)

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.setColor(java.awt.Color)"""
        super(__DistanceFieldGenerator, self).setColor(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator