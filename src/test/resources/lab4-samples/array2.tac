____TakeArray:
	BeginFunc 116 ;
	_tmp0 = 4 ;
	_tmp1 = 0 ;
	_tmp2 = *(x) ;
	_tmp3 = _tmp0 < _tmp1 ;
	_tmp4 = _tmp2 < _tmp0 ;
	_tmp5 = _tmp2 == _tmp0 ;
	_tmp6 = _tmp4 || _tmp5 ;
	_tmp7 = _tmp6 || _tmp3 ;
	IfZ _tmp7 Goto _L0 ;
	_tmp8 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp8 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L0:
	_tmp9 = 4 ;
	_tmp10 = _tmp0 * _tmp9 ;
	_tmp11 = _tmp10 + _tmp9 ;
	_tmp12 = x + _tmp11 ;
	_tmp13 = *(_tmp12) ;
	PushParam _tmp13 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp14 = 5 ;
	_tmp15 = 0 ;
	_tmp16 = *(x) ;
	_tmp17 = _tmp14 < _tmp15 ;
	_tmp18 = _tmp16 < _tmp14 ;
	_tmp19 = _tmp16 == _tmp14 ;
	_tmp20 = _tmp18 || _tmp19 ;
	_tmp21 = _tmp20 || _tmp17 ;
	IfZ _tmp21 Goto _L1 ;
	_tmp22 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp22 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L1:
	_tmp23 = 4 ;
	_tmp24 = _tmp14 * _tmp23 ;
	_tmp25 = _tmp24 + _tmp23 ;
	_tmp26 = x + _tmp25 ;
	_tmp27 = *(_tmp26) ;
	PushParam _tmp27 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp28 = *(x) ;
	PushParam _tmp28 ;
	LCall _PrintInt ;
	PopParams 4 ;
	EndFunc ;
____MakeArray:
	BeginFunc 108 ;
	_tmp29 = 4 ;
	_tmp30 = 0 ;
	_tmp31 = size < _tmp30 ;
	_tmp32 = size == _tmp30 ;
	_tmp33 = _tmp31 || _tmp32 ;
	IfZ _tmp33 Goto _L2 ;
	_tmp34 = "Decaf runtime error: Array size is <= 0\n" ;
	PushParam _tmp34 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L2:
	_tmp35 = size * _tmp29 ;
	_tmp36 = _tmp29 + _tmp35 ;
	PushParam _tmp36 ;
	_tmp37 = LCall _Alloc ;
	PopParams 4 ;
	*(_tmp37) = size ;
	b = _tmp37 ;
	_tmp38 = 5 ;
	_tmp39 = 0 ;
	_tmp40 = 0 ;
	_tmp41 = *(b) ;
	_tmp42 = _tmp39 < _tmp40 ;
	_tmp43 = _tmp41 < _tmp39 ;
	_tmp44 = _tmp41 == _tmp39 ;
	_tmp45 = _tmp43 || _tmp44 ;
	_tmp46 = _tmp45 || _tmp42 ;
	IfZ _tmp46 Goto _L3 ;
	_tmp47 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp47 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L3:
	_tmp48 = 4 ;
	_tmp49 = _tmp39 * _tmp48 ;
	_tmp50 = _tmp49 + _tmp48 ;
	_tmp51 = b + _tmp50 ;
	*(_tmp51) = _tmp38 ;
	_tmp52 = *(_tmp51) ;
	Return b ;
	EndFunc ;
main:
	BeginFunc 268 ;
	_tmp53 = 10 ;
	_tmp54 = 4 ;
	_tmp55 = 0 ;
	_tmp56 = _tmp53 < _tmp55 ;
	_tmp57 = _tmp53 == _tmp55 ;
	_tmp58 = _tmp56 || _tmp57 ;
	IfZ _tmp58 Goto _L4 ;
	_tmp59 = "Decaf runtime error: Array size is <= 0\n" ;
	PushParam _tmp59 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L4:
	_tmp60 = _tmp53 * _tmp54 ;
	_tmp61 = _tmp54 + _tmp60 ;
	PushParam _tmp61 ;
	_tmp62 = LCall _Alloc ;
	PopParams 4 ;
	*(_tmp62) = _tmp53 ;
	y = _tmp62 ;
	_tmp63 = 3 ;
	_tmp64 = 4 ;
	_tmp65 = 0 ;
	_tmp66 = *(y) ;
	_tmp67 = _tmp64 < _tmp65 ;
	_tmp68 = _tmp66 < _tmp64 ;
	_tmp69 = _tmp66 == _tmp64 ;
	_tmp70 = _tmp68 || _tmp69 ;
	_tmp71 = _tmp70 || _tmp67 ;
	IfZ _tmp71 Goto _L5 ;
	_tmp72 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp72 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L5:
	_tmp73 = 4 ;
	_tmp74 = _tmp64 * _tmp73 ;
	_tmp75 = _tmp74 + _tmp73 ;
	_tmp76 = y + _tmp75 ;
	*(_tmp76) = _tmp63 ;
	_tmp77 = *(_tmp76) ;
	_tmp78 = 4 ;
	_tmp79 = 5 ;
	_tmp80 = 0 ;
	_tmp81 = *(y) ;
	_tmp82 = _tmp79 < _tmp80 ;
	_tmp83 = _tmp81 < _tmp79 ;
	_tmp84 = _tmp81 == _tmp79 ;
	_tmp85 = _tmp83 || _tmp84 ;
	_tmp86 = _tmp85 || _tmp82 ;
	IfZ _tmp86 Goto _L6 ;
	_tmp87 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp87 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L6:
	_tmp88 = 4 ;
	_tmp89 = _tmp79 * _tmp88 ;
	_tmp90 = _tmp89 + _tmp88 ;
	_tmp91 = y + _tmp90 ;
	*(_tmp91) = _tmp78 ;
	_tmp92 = *(_tmp91) ;
	PushParam y ;
	LCall ____TakeArray ;
	PopParams 4 ;
	_tmp93 = 10 ;
	PushParam _tmp93 ;
	_tmp94 = LCall ____MakeArray ;
	PopParams 4 ;
	b = _tmp94 ;
	_tmp95 = 0 ;
	_tmp96 = 0 ;
	_tmp97 = *(b) ;
	_tmp98 = _tmp95 < _tmp96 ;
	_tmp99 = _tmp97 < _tmp95 ;
	_tmp100 = _tmp97 == _tmp95 ;
	_tmp101 = _tmp99 || _tmp100 ;
	_tmp102 = _tmp101 || _tmp98 ;
	IfZ _tmp102 Goto _L7 ;
	_tmp103 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp103 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L7:
	_tmp104 = 4 ;
	_tmp105 = _tmp95 * _tmp104 ;
	_tmp106 = _tmp105 + _tmp104 ;
	_tmp107 = b + _tmp106 ;
	_tmp108 = *(_tmp107) ;
	PushParam _tmp108 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp109 = *(b) ;
	PushParam _tmp109 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp110 = 5 ;
	PushParam _tmp110 ;
	_tmp111 = LCall ____MakeArray ;
	PopParams 4 ;
	_tmp112 = *(_tmp111) ;
	PushParam _tmp112 ;
	LCall _PrintInt ;
	PopParams 4 ;
	EndFunc ;