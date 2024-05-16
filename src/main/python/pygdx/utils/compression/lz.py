from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.compression.lz.InWindow as __InWindow
__InWindow = __InWindow
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InWindow():
    """com.badlogic.gdx.utils.compression.lz.InWindow"""
 
    @staticmethod
    def __wrap(java_value: __InWindow) -> 'InWindow':
        return InWindow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InWindow):
        """
        Dynamic initializer for InWindow.
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
    def MovePos(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.MovePos() throws java.io.IOException"""
        super(InWindow, self).MovePos()

    @overload
    def Create(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.Create(int,int,int)"""
        super(__InWindow, self).Create(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lz.InWindow()"""
        val = __InWindow()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def SetStream(self, arg0: 'InputStream'):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.SetStream(java.io.InputStream)"""
        super(__InWindow, self).SetStream(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def ReleaseStream(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReleaseStream()"""
        super(InWindow, self).ReleaseStream()

    @overload
    def MoveBlock(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.MoveBlock()"""
        super(InWindow, self).MoveBlock()

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
    def ReduceOffsets(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReduceOffsets(int)"""
        super(__InWindow, self).ReduceOffsets(__int.valueOf(arg0))

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
    def GetNumAvailableBytes(self) -> int:
        """public int com.badlogic.gdx.utils.compression.lz.InWindow.GetNumAvailableBytes()"""
        return int.__wrap(super(InWindow, self).GetNumAvailableBytes())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.Init() throws java.io.IOException"""
        super(InWindow, self).Init()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lz.InWindow()"""
        val = __InWindow()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def GetMatchLen(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.utils.compression.lz.InWindow.GetMatchLen(int,int,int)"""
        return int.__wrap(super(__InWindow, self).GetMatchLen(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def ReadBlock(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReadBlock() throws java.io.IOException"""
        super(InWindow, self).ReadBlock()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def GetIndexByte(self, arg0: int) -> int:
        """public byte com.badlogic.gdx.utils.compression.lz.InWindow.GetIndexByte(int)"""
        return int.__wrap(super(__InWindow, self).GetIndexByte(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lz.InWindow
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.compression.lz.InWindow as __InWindow
__InWindow = __InWindow
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InWindow():
    """com.badlogic.gdx.utils.compression.lz.InWindow"""
 
    @staticmethod
    def __wrap(java_value: __InWindow) -> 'InWindow':
        return InWindow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InWindow):
        """
        Dynamic initializer for InWindow.
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
    def MovePos(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.MovePos() throws java.io.IOException"""
        super(InWindow, self).MovePos()

    @overload
    def Create(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.Create(int,int,int)"""
        super(__InWindow, self).Create(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lz.InWindow()"""
        val = __InWindow()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def SetStream(self, arg0: 'InputStream'):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.SetStream(java.io.InputStream)"""
        super(__InWindow, self).SetStream(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def ReleaseStream(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReleaseStream()"""
        super(InWindow, self).ReleaseStream()

    @overload
    def MoveBlock(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.MoveBlock()"""
        super(InWindow, self).MoveBlock()

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
    def ReduceOffsets(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReduceOffsets(int)"""
        super(__InWindow, self).ReduceOffsets(__int.valueOf(arg0))

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
    def GetNumAvailableBytes(self) -> int:
        """public int com.badlogic.gdx.utils.compression.lz.InWindow.GetNumAvailableBytes()"""
        return int.__wrap(super(InWindow, self).GetNumAvailableBytes())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.Init() throws java.io.IOException"""
        super(InWindow, self).Init()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lz.InWindow()"""
        val = __InWindow()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def GetMatchLen(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.utils.compression.lz.InWindow.GetMatchLen(int,int,int)"""
        return int.__wrap(super(__InWindow, self).GetMatchLen(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def ReadBlock(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReadBlock() throws java.io.IOException"""
        super(InWindow, self).ReadBlock()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def GetIndexByte(self, arg0: int) -> int:
        """public byte com.badlogic.gdx.utils.compression.lz.InWindow.GetIndexByte(int)"""
        return int.__wrap(super(__InWindow, self).GetIndexByte(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lz.InWindow 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lz.BinTree
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.compression.lz.BinTree as __BinTree
__BinTree = __BinTree
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.compression.lz.InWindow as __InWindow
__InWindow = __InWindow
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BinTree(__InWindow, InWindow):
    """com.badlogic.gdx.utils.compression.lz.BinTree"""
 
    @staticmethod
    def __wrap(java_value: __BinTree) -> 'BinTree':
        return BinTree(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BinTree):
        """
        Dynamic initializer for BinTree.
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
    def Create(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.Create(int,int,int)"""
        super(__InWindow, self).Create(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.lz.BinTree.Init() throws java.io.IOException"""
        super(BinTree, self).Init()

    @override
    @overload
    def ReduceOffsets(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReduceOffsets(int)"""
        super(__InWindow, self).ReduceOffsets(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lz.BinTree()"""
        val = __BinTree()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def Skip(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.BinTree.Skip(int) throws java.io.IOException"""
        super(__BinTree, self).Skip(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def SetStream(self, arg0: 'InputStream'):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.SetStream(java.io.InputStream)"""
        super(__InWindow, self).SetStream(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def SetCutValue(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.BinTree.SetCutValue(int)"""
        super(__BinTree, self).SetCutValue(__int.valueOf(arg0))

    @overload
    def GetIndexByte(self, arg0: int) -> int:
        """public byte com.badlogic.gdx.utils.compression.lz.InWindow.GetIndexByte(int)"""
        return int.__wrap(super(__InWindow, self).GetIndexByte(__int.valueOf(arg0)))

    @override
    @overload
    def MovePos(self):
        """public void com.badlogic.gdx.utils.compression.lz.BinTree.MovePos() throws java.io.IOException"""
        super(BinTree, self).MovePos()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def GetNumAvailableBytes(self) -> int:
        """public int com.badlogic.gdx.utils.compression.lz.InWindow.GetNumAvailableBytes()"""
        return int.__wrap(super(InWindow, self).GetNumAvailableBytes())

    @overload
    def Create(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lz.BinTree.Create(int,int,int,int)"""
        return bool.__wrap(super(__BinTree, self).Create(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lz.BinTree()"""
        val = __BinTree()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def SetType(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.BinTree.SetType(int)"""
        super(__BinTree, self).SetType(__int.valueOf(arg0))

    @override
    @overload
    def ReadBlock(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReadBlock() throws java.io.IOException"""
        super(InWindow, self).ReadBlock()

    @override
    @overload
    def MoveBlock(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.MoveBlock()"""
        super(InWindow, self).MoveBlock()

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
    def ReleaseStream(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReleaseStream()"""
        super(InWindow, self).ReleaseStream()

    @overload
    def GetMatchLen(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.utils.compression.lz.InWindow.GetMatchLen(int,int,int)"""
        return int.__wrap(super(__InWindow, self).GetMatchLen(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def GetMatches(self, arg0: 'int') -> int:
        """public int com.badlogic.gdx.utils.compression.lz.BinTree.GetMatches(int[]) throws java.io.IOException"""
        return int.__wrap(super(__BinTree, self).GetMatches(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lz.OutWindow
from builtins import str
import com.badlogic.gdx.utils.compression.lz.OutWindow as __OutWindow
__OutWindow = __OutWindow
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class OutWindow():
    """com.badlogic.gdx.utils.compression.lz.OutWindow"""
 
    @staticmethod
    def __wrap(java_value: __OutWindow) -> 'OutWindow':
        return OutWindow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OutWindow):
        """
        Dynamic initializer for OutWindow.
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
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lz.OutWindow()"""
        val = __OutWindow()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def Init(self, arg0: bool):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.Init(boolean)"""
        super(__OutWindow, self).Init(__boolean.valueOf(arg0))

    @overload
    def ReleaseStream(self):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.ReleaseStream() throws java.io.IOException"""
        super(OutWindow, self).ReleaseStream()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def PutByte(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.PutByte(byte) throws java.io.IOException"""
        super(__OutWindow, self).PutByte(__byte.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def Flush(self):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.Flush() throws java.io.IOException"""
        super(OutWindow, self).Flush()

    @overload
    def SetStream(self, arg0: 'OutputStream'):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.SetStream(java.io.OutputStream) throws java.io.IOException"""
        super(__OutWindow, self).SetStream(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lz.OutWindow()"""
        val = __OutWindow()
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

    @overload
    def Create(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.Create(int)"""
        super(__OutWindow, self).Create(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def GetByte(self, arg0: int) -> int:
        """public byte com.badlogic.gdx.utils.compression.lz.OutWindow.GetByte(int)"""
        return int.__wrap(super(__OutWindow, self).GetByte(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def CopyBlock(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.CopyBlock(int,int) throws java.io.IOException"""
        super(__OutWindow, self).CopyBlock(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))