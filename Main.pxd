

from mcbasecpp.base_global cimport MAT, SEGMENT_DICT
from libcpp cimport bool
from mcbasecpp.corProject cimport corProject

cdef bool doHotSpotDetectionG
cdef bool hotSpotFoundAndFixedG 
cdef SEGMENT_DICT[double] backupShiftwtSA
cdef rule_section_main_fun()
cdef rule_fragmented_main_fun()
cdef backup_and_reset_shiftwts_fun()
cdef restore_shiftwts_from_backup_fun()
cdef etch_correction_setup_fun()
cdef etch_final_checks_and_judgement_fun()
cdef create_default_projection_py_object_fun(corProject *fragmentPY)
cdef correction_setup_fun(inHotSpotFixCall, mssGroupingType, mssSegmentFlag)
cdef adjust_shiftwt_limits_fun(doSearchBasedClamping, doEndVertRunClamping,minEnd, maxEnd,minVert, maxVert,minRun, maxRun,minSpace=*,minWidth=*,initialize=*)
cdef setup_check_figures_fun(inHotSpotFixCall=*)
cdef update_check_figures_fun()
cdef apply_all_perturbwts_to_shiftwts_fun()
cdef apply_perturbwt_to_shiftwt_fun(numPwtClampingValues, MAT[double] &perturbwtMaxA, MAT[double] &perturbwtMinA)
cdef extend_correction_under_avoid_ring_fun()
cdef init_perturbwt_clamping_arrays_fun(MAT[double] &perturbwtMaxA, MAT[double] &perturbwtMinA)
cdef this_seg_apply_perturb_clamping_fun(pwt, numPwtClampingValues, MAT[double] &perturbwtMaxA, MAT[double] &perturbwtMinA)
cdef final_checks_and_judgement_fun()
cdef mbopc_setup_fun(corProject *fragmentPY, fragmentAfs, exitAfterFragmented, xtemplateFragmentedEnabled, userTypeOfFragmentedMarks)
cdef fragment_afs_for_mrc_fun()
cdef perturbbox_correction_fun(iter)
cdef fast_descent_correction_first_pass_fun(iter)
cdef fast_descent_correction_second_pass_fun()
cdef fast_descent_correction_third_pass_fun()
cdef checks_and_judgement_after_correction_fun()
cdef af_check_jog_on45_deg_segs_fun(maxJogLen)
cdef show_correction_sites_and_fragmented_sites_fun()
cdef copy_fragmented_from_ref_fun(corLayer, xorLayer)
cdef copy_shiftwt_from_ref_fun(corLayer, refLayer, copy_shiftwt_mode)
cdef setup_tolerance_based_opc_fun(corProject *tolerancebasedopcPY)
cdef set_i_terf_fun(iter)
cdef init_hot_spot_fix_fun()
cdef dumbbell_contact_correction_refix_fun()
cdef apply_hot_spot_fix_with_matrix_solver_fun(iter)
cdef max_positive_shiftwt_fun(userType)
