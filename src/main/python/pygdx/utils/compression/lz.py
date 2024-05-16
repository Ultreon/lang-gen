from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.io.InputStream as InputStream
import com.badlogic.gdx.utils.compression.lz.InWindow as _InWindow
_InWindow = _InWindow
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InWindow():
    """com.badlogic.gdx.utils.compression.lz.InWindow"""
 
    @staticmethod
    def _wrap(java_value: _InWindow) -> 'InWindow':
        return InWindow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InWindow):
        """
        Dynamic initializer for InWindow.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InWindow__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InWindow__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def GetIndexByte(self, arg0: int) -> int:
        """public byte com.badlogic.gdx.utils.compression.lz.InWindow.GetIndexByte(int)"""
        return int._wrap(super(_InWindow, self).GetIndexByte(_int.valueOf(arg0)))

    @overload
    def MovePos(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.MovePos() throws java.io.IOException"""
        super(InWindow, self).MovePos()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lz.InWindow()"""
        val = _InWindow()
        self.__wrapper = val

    @overload
    def SetStream(self, arg0: 'InputStream'):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.SetStream(java.io.InputStream)"""
        super(_InWindow, self).SetStream(arg0)

    @overload
    def ReleaseStream(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReleaseStream()"""
        super(InWindow, self).ReleaseStream()

    @overload
    def GetNumAvailableBytes(self) -> int:
        """public int com.badlogic.gdx.utils.compression.lz.InWindow.GetNumAvailableBytes()"""
        return int._wrap(super(InWindow, self).GetNumAvailableBytes())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def MoveBlock(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.MoveBlock()"""
        super(InWindow, self).MoveBlock()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def Create(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.Create(int,int,int)"""
        super(_InWindow, self).Create(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def GetMatchLen(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.utils.compression.lz.InWindow.GetMatchLen(int,int,int)"""
        return int._wrap(super(_InWindow, self).GetMatchLen(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.Init() throws java.io.IOException"""
        super(InWindow, self).Init()

    @overload
    def ReduceOffsets(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReduceOffsets(int)"""
        super(_InWindow, self).ReduceOffsets(_int.valueOf(arg0))

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
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lz.InWindow()"""
        val = _InWindow()
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

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lz.InWindow
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.io.InputStream as InputStream
import com.badlogic.gdx.utils.compression.lz.InWindow as _InWindow
_InWindow = _InWindow
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InWindow():
    """com.badlogic.gdx.utils.compression.lz.InWindow"""
 
    @staticmethod
    def _wrap(java_value: _InWindow) -> 'InWindow':
        return InWindow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InWindow):
        """
        Dynamic initializer for InWindow.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InWindow__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InWindow__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def GetIndexByte(self, arg0: int) -> int:
        """public byte com.badlogic.gdx.utils.compression.lz.InWindow.GetIndexByte(int)"""
        return int._wrap(super(_InWindow, self).GetIndexByte(_int.valueOf(arg0)))

    @overload
    def MovePos(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.MovePos() throws java.io.IOException"""
        super(InWindow, self).MovePos()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lz.InWindow()"""
        val = _InWindow()
        self.__wrapper = val

    @overload
    def SetStream(self, arg0: 'InputStream'):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.SetStream(java.io.InputStream)"""
        super(_InWindow, self).SetStream(arg0)

    @overload
    def ReleaseStream(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReleaseStream()"""
        super(InWindow, self).ReleaseStream()

    @overload
    def GetNumAvailableBytes(self) -> int:
        """public int com.badlogic.gdx.utils.compression.lz.InWindow.GetNumAvailableBytes()"""
        return int._wrap(super(InWindow, self).GetNumAvailableBytes())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def MoveBlock(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.MoveBlock()"""
        super(InWindow, self).MoveBlock()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def Create(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.Create(int,int,int)"""
        super(_InWindow, self).Create(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def GetMatchLen(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.utils.compression.lz.InWindow.GetMatchLen(int,int,int)"""
        return int._wrap(super(_InWindow, self).GetMatchLen(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.Init() throws java.io.IOException"""
        super(InWindow, self).Init()

    @overload
    def ReduceOffsets(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReduceOffsets(int)"""
        super(_InWindow, self).ReduceOffsets(_int.valueOf(arg0))

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
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lz.InWindow()"""
        val = _InWindow()
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

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lz.InWindow 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lz.OutWindow
from builtins import str
import com.badlogic.gdx.utils.compression.lz.OutWindow as _OutWindow
_OutWindow = _OutWindow
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.io.OutputStream as OutputStream
import java.lang.Integer as _int
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OutWindow():
    """com.badlogic.gdx.utils.compression.lz.OutWindow"""
 
    @staticmethod
    def _wrap(java_value: _OutWindow) -> 'OutWindow':
        return OutWindow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OutWindow):
        """
        Dynamic initializer for OutWindow.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OutWindow__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OutWindow__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def GetByte(self, arg0: int) -> int:
        """public byte com.badlogic.gdx.utils.compression.lz.OutWindow.GetByte(int)"""
        return int._wrap(super(_OutWindow, self).GetByte(_int.valueOf(arg0)))

    @overload
    def ReleaseStream(self):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.ReleaseStream() throws java.io.IOException"""
        super(OutWindow, self).ReleaseStream()

    @overload
    def CopyBlock(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.CopyBlock(int,int) throws java.io.IOException"""
        super(_OutWindow, self).CopyBlock(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def Flush(self):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.Flush() throws java.io.IOException"""
        super(OutWindow, self).Flush()

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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lz.OutWindow()"""
        val = _OutWindow()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def Create(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.Create(int)"""
        super(_OutWindow, self).Create(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lz.OutWindow()"""
        val = _OutWindow()
        self.__wrapper = val

    @overload
    def PutByte(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.PutByte(byte) throws java.io.IOException"""
        super(_OutWindow, self).PutByte(_byte.valueOf(arg0))

    @overload
    def SetStream(self, arg0: 'OutputStream'):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.SetStream(java.io.OutputStream) throws java.io.IOException"""
        super(_OutWindow, self).SetStream(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def Init(self, arg0: bool):
        """public void com.badlogic.gdx.utils.compression.lz.OutWindow.Init(boolean)"""
        super(_OutWindow, self).Init(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lz.BinTree
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.utils.compression.lz.BinTree as _BinTree
_BinTree = _BinTree
import java.io.InputStream as InputStream
from builtins import bool
import com.badlogic.gdx.utils.compression.lz.InWindow as _InWindow
_InWindow = _InWindow
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BinTree():
    """com.badlogic.gdx.utils.compression.lz.BinTree"""
 
    @staticmethod
    def _wrap(java_value: _BinTree) -> 'BinTree':
        return BinTree(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BinTree):
        """
        Dynamic initializer for BinTree.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BinTree__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BinTree__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def SetStream(self, arg0: 'InputStream'):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.SetStream(java.io.InputStream)"""
        super(_InWindow, self).SetStream(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lz.BinTree()"""
        val = _BinTree()
        self.__wrapper = val

    @override
    @overload
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.lz.BinTree.Init() throws java.io.IOException"""
        super(BinTree, self).Init()

    @override
    @overload
    def GetNumAvailableBytes(self) -> int:
        """public int com.badlogic.gdx.utils.compression.lz.InWindow.GetNumAvailableBytes()"""
        return int._wrap(super(InWindow, self).GetNumAvailableBytes())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ReduceOffsets(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReduceOffsets(int)"""
        super(_InWindow, self).ReduceOffsets(_int.valueOf(arg0))

    @overload
    def SetType(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.BinTree.SetType(int)"""
        super(_BinTree, self).SetType(_int.valueOf(arg0))

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
    def GetMatches(self, arg0: 'int') -> int:
        """public int com.badlogic.gdx.utils.compression.lz.BinTree.GetMatches(int[]) throws java.io.IOException"""
        return int._wrap(super(_BinTree, self).GetMatches(arg0))

    @override
    @overload
    def MovePos(self):
        """public void com.badlogic.gdx.utils.compression.lz.BinTree.MovePos() throws java.io.IOException"""
        super(BinTree, self).MovePos()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def GetIndexByte(self, arg0: int) -> int:
        """public byte com.badlogic.gdx.utils.compression.lz.InWindow.GetIndexByte(int)"""
        return int._wrap(super(_InWindow, self).GetIndexByte(_int.valueOf(arg0)))

    @override
    @overload
    def Create(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.Create(int,int,int)"""
        super(_InWindow, self).Create(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def ReadBlock(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReadBlock() throws java.io.IOException"""
        super(InWindow, self).ReadBlock()

    @overload
    def GetMatchLen(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.utils.compression.lz.InWindow.GetMatchLen(int,int,int)"""
        return int._wrap(super(_InWindow, self).GetMatchLen(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def MoveBlock(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.MoveBlock()"""
        super(InWindow, self).MoveBlock()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def SetCutValue(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.BinTree.SetCutValue(int)"""
        super(_BinTree, self).SetCutValue(_int.valueOf(arg0))

    @override
    @overload
    def ReleaseStream(self):
        """public void com.badlogic.gdx.utils.compression.lz.InWindow.ReleaseStream()"""
        super(InWindow, self).ReleaseStream()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lz.BinTree()"""
        val = _BinTree()
        self.__wrapper = val

    @overload
    def Skip(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.lz.BinTree.Skip(int) throws java.io.IOException"""
        super(_BinTree, self).Skip(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def Create(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lz.BinTree.Create(int,int,int,int)"""
        return bool._wrap(super(_BinTree, self).Create(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())