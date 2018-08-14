/*
 * MATLAB Compiler: 6.5 (R2017b)
 * Date: Tue Aug 14 10:32:25 2018
 * Arguments:
 * "-B""macro_default""-W""lib:ParResPkgNew""-T""link:lib""-d""/Users/markhigger
 * /Documents/NKI/mHigger_NKI/mtlbPkgTest/ParResPkgNew/for_testing""-v""/Users/m
 * arkhigger/Documents/MATLAB/ParRes.m"
 */

#ifndef __ParResPkgNew_h
#define __ParResPkgNew_h 1

#if defined(__cplusplus) && !defined(mclmcrrt_h) && defined(__linux__)
#  pragma implementation "mclmcrrt.h"
#endif
#include "mclmcrrt.h"
#ifdef __cplusplus
extern "C" {
#endif

/* This symbol is defined in shared libraries. Define it here
 * (to nothing) in case this isn't a shared library. 
 */
#ifndef LIB_ParResPkgNew_C_API 
#define LIB_ParResPkgNew_C_API /* No special import/export declaration */
#endif

/* GENERAL LIBRARY FUNCTIONS -- START */

extern LIB_ParResPkgNew_C_API 
bool MW_CALL_CONV ParResPkgNewInitializeWithHandlers(
       mclOutputHandlerFcn error_handler, 
       mclOutputHandlerFcn print_handler);

extern LIB_ParResPkgNew_C_API 
bool MW_CALL_CONV ParResPkgNewInitialize(void);

extern LIB_ParResPkgNew_C_API 
void MW_CALL_CONV ParResPkgNewTerminate(void);

extern LIB_ParResPkgNew_C_API 
void MW_CALL_CONV ParResPkgNewPrintStackTrace(void);

/* GENERAL LIBRARY FUNCTIONS -- END */

/* C INTERFACE -- MLX WRAPPERS FOR USER-DEFINED MATLAB FUNCTIONS -- START */

extern LIB_ParResPkgNew_C_API 
bool MW_CALL_CONV mlxParRes(int nlhs, mxArray *plhs[], int nrhs, mxArray *prhs[]);

/* C INTERFACE -- MLX WRAPPERS FOR USER-DEFINED MATLAB FUNCTIONS -- END */

/* C INTERFACE -- MLF WRAPPERS FOR USER-DEFINED MATLAB FUNCTIONS -- START */

extern LIB_ParResPkgNew_C_API bool MW_CALL_CONV mlfParRes(int nargout, mxArray** R, mxArray* R1, mxArray* R2);

#ifdef __cplusplus
}
#endif
/* C INTERFACE -- MLF WRAPPERS FOR USER-DEFINED MATLAB FUNCTIONS -- END */

#endif
