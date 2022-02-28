.. post:: 25 Feb 2022
   :tags: research, tips, newbs, education
   :category: computational science

So you're starting a research project, where do you begin?
==========================================================

Overview
--------

.. companion article, So you're supervising someone who is doing their first research project, help!
.. Welcome to explorer school, you will are the instructor

This post is intended for anyone starting out in research and development with a computational bent, whether in a science (e.g. computational biology) or engineering context. In particular, it is focussed on the research process that leads to new tools and analysis methods.

So far, your exposure to knowledge discovery has likely been limited to textbook descriptions of how "thing x" was discovered. While being a consumer of such knowledge discovery is often challenging, the account you read is a highly distilled version of what happened. Being the original discoverer is more complicated.

Take heart! Discoveries are not arrived at in completed form. By employing a systematic approach, we incrementally assemble the pieces to draw that new insight and develop something new and valuable. What follows is a sketch of my process.

Structure is key
----------------

I break the process into three questions you must answer: *Why*, *What* and *How*. These correspond to:

- *Why* is there a problem?
- *What* is the problem?
- *How*  will you solve it?

But before we delve into those, you need to answer two other questions. What form does your final output need to be? When is that due??? If you perform research and make a brilliant discovery but don't write a systematic description of how you made that discovery, it is the same as not doing anything.

Establish what form your **final** output should be in (talk to your supervisor). Your project plan should be something that directly references that and makes delivering it easy.

.. _the_why:

The Why
-------

.. epigraph::

    Why does the problem even exist? Why is it a problem worthy of your attention? Why hasn't it already been solved? Answering all these is your justification for doing the work and, at the very least, should make you comfortable you may be doing something worthwhile.

This is the big picture part of the project and should proceed everything else. Identifying the existence of a problem requires you have a solid understanding of the domain. At this stage in your career, it's quite likely that you have been "given" the problem. But once you take it, it becomes **your** problem [#]_. In other words, the onus is on you to understand the background material that led to defining the problem. Ultimately, this requires reading about what others have done.

What are the existing solutions, and why are those inadequate?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. epigraph::

    When you examine existing solutions, take a big picture view. What are the core algorithms they implement? How do the algorithms relate to each other? What are their inputs and outputs? Do they have a killer flaw or are they blocking a key opportunity?

Establishing :ref:`the_why` almost always requires in-depth of consideration of what others have already done. So what are the existing solutions, and why are they not good enough? Study them carefully to look for a new investigation avenue and frame your response to :ref:`the_what`. Pay particular attention to how prior work was done, as that defines a minimum standard you must meet to have your work taken seriously.

.. note::

    Criticising the work of others is a "core business" in science and engineering. That said, consider these three crucial qualifiers when you frame that criticism.

    #. What is the **evidence** the solutions are inadequate? (That evidence can be measurement, or a theoretical property.)
    #. The prior work was likely developed against different technological inputs [#]_.
    #. Much of the information available to us now may not have been known to the authors of the original work.

    A critique of the work of others is based on what we know now. So be respectful. I guarantee you that someone will be casting their critical eye over what you do in the future.

.. _the_what:

The What
--------

Your proposition
^^^^^^^^^^^^^^^^

.. epigraph::

    What is the problem being solved? Try and express this as succinctly as possible. This statement may need to be updated as your knowledge of the domain increases [#]_. Critically, the statement must be something you can actually solve.

This is the nitty-gritty and why you're reading this. It is your statement of what YOU will achieve and stems from the careful consideration described above. The framing of "what" problem you will solve can benefit from identifying both its inputs and outputs. Meaning, what is the input data (including where the data will, or can, come from)?. What is the output you will produce?

.. note:: Together, the inputs and outputs define your target audience.

What you propose should explicitly address at least part of the shortcomings of existing solutions you identified in :ref:`the_why`.

Its value
^^^^^^^^^

.. epigraph::

    What is the value [#]_ of your proposed solution? To establish this value, be clear on the output of your work and why it will be more valuable than what exists. Will it improve prediction accuracy? Will it require magnitudes less computing resources? Will it be more maintainable?

Your answer should reflect the significance you have attributed to the shortcomings of existing approaches and your argument of the benefit to the target audience.

But that thinking is contingent upon the successful completion of the project. The value of a project also comes from what can be learned *if it fails*. Prepare yourself for the possibility that your proposal will not deliver on this promised value. 

Here's a crucial reality-check -- is a negative answer still interesting?

At the very least, you do not want the project to fail because you did not ensure the :ref:`correctness <correctness>` of your implementation or execution.

.. _the_how:

The How
-------

Your solution
^^^^^^^^^^^^^

.. epigraph::

    How will you tackle the inadequacy of existing solution(s)?

- Big-picture view of the core algorithms to be implemented
- What input data does each algorithmic component need, and how will you get it?
- What data properties must you account for?
- What other resources does the project need?

.. _correctness:

Making it believable
^^^^^^^^^^^^^^^^^^^^

.. epigraph::

    How will you check correctness?

- What properties should be guaranteed?
- What data property corner cases can you identify and how should the algorithm behave in those situations?
- Are there ground truths you can rely on (e.g. from theory)?

.. _measure_performance:

Measure performance
^^^^^^^^^^^^^^^^^^^

.. epigraph::

    What measurable quantities best capture performance?

- What competitors will you also benchmark?
- What "experimental design" will you use that allows concluding your algorithm is a good choice over competitors?
- Identify appropriate metrics to highlight the different attributes, adopting standards of the domain wherever possible

Identify milestones
^^^^^^^^^^^^^^^^^^^

- Stages towards project completion
- Define termination project condition(s)

Principles of Pragmatic Project Execution
-----------------------------------------

Plan, do, repeat
^^^^^^^^^^^^^^^^

.. warning:: Your time is your most valuable currency. Spend it wisely.

Newbies are very tempted to jump straight into the "doing" part of a new project. Working furiously gives immediate reward and a sense of achievement. But without direction, you are probably wasting your time.

.. tip:: Plan first, then do.

Your project plan begins by addressing the issues listed above. Convert those responses into a flowchart where the nodes are "processes" in your research project (e.g. data sampling). This flow chart will be a dynamic figure, meaning that you will update and refine it as you go. It is also a figure that you will likely employ when you explain the project to an audience, either in a conference presentation or a research / technical paper.

Optimise for the minimal project duration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. epigraph::

    Can you build the project order of execution so that the best outcome is achieved with minimal effort (i.e., breaking the problem down so that you incrementally prototype to the final solution)?

If you can break a project into components, what is the dependency structure among them? Put the most difficult ones as close to the beginning of a project execution plan as possible.

It requires some significant mental effort to see how you can break a problem down into parts that can be solved independently -- having done that, which is most central to your goal? Tackling that must be a priority.

.. tip:: Remember, you want to fail fast!

Fast prototyping
^^^^^^^^^^^^^^^^

.. epigraph::

    "Premature optimisation is the root of all evil."

    ---  Donald Knuth

    "Seriously!"

    --- Gavin

Once you have a project sketch, you should aim to prototype the entire workflow [#]_ as fast as possible, including getting to the point of quantifying performance. "Fast" refers to both implementation time (crude code is the goal) AND computation time with the latter often achieved by using a minimal amount of data.

You will learn a lot from this process, including the types of tests you will need to write to ensure :ref:`correctness <correctness>`.

Iterate the flow, baby!
^^^^^^^^^^^^^^^^^^^^^^^

.. epigraph::

    Repeat the above steps.

In the beginning, there may be many things you don't understand. Highlight the things you don't understand and discuss them with your supervisor and/or colleagues.

What if your approach is impossible?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. epigraph::

    How will you decide if the project is infeasible? What is your backup plan?

Make sure your project can produce something. The form this might take will differ between a science and an engineering project. Discuss with your supervisor for specifics.

How will you decide when you're done?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. epigraph::

    Is there a clear end-point? How will you avoid the infinite loop of tweaking?

What if your work does not "outperform" competitors? Is knowing this still valuable [#]_? There's a strong urge to try "just one more thing" in this situation. In a well designed and executed project, the futility of such tweaking should be apparent. But it requires strength of character to call it quits. You don't want to waste time polishing a |:poop:|.

If it does "outperform" competitors, happy days! You still have to avoid excessive polishing. The relevant saying here is "great is the enemy of good", i.e. don't be a perfectionist.

Don't isolate yourself
^^^^^^^^^^^^^^^^^^^^^^

.. epigraph::

    How often and with who will you discuss your project?

Too often, junior researchers / engineers think they need to solve the entirety of a project by themselves ... in one massive go. Don't do that!

Science and engineering deliver consistently better results when multiple brains are involved. Discussions with others help you develop your understanding and provide a crucial perspective that can help you decide when you may be wasting your time pursuing an approach that cannot work or when a superior approach is possible. Your supervisor provides a crucial point of contact for such discussions. In my view, however, they should not be the only person you discuss things with.

Tackling the inevitable problems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. epigraph::

    Troubleshoot! If the process of identifying the minimal example of a problem does not expose the solution, then find someone to discuss it with.

An essential skill is knowing what *you* don't know and being able to identify someone else with the necessary knowledge. That said, another critical skill is trying to solve a problem yourself before you ask someone else for help. Prior to asking someone else for help, answer the following questions:

#. Have you seriously tried?
#. What steps have you taken that you can show to the person you're about to ask?
#. What's in it for them? In other words, why should they spend their time helping you solve **your** problem?

Often, just discussing the problem with someone else is sufficient for you to identify the solution.

.. tip:: Give yourself a break from working on a hard problem. Do something else for a while so that you stop thinking about it. A fresh mind solves more problems than a tired one.

Don't forget to enjoy yourself
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. epigraph::

    Research should enrich your life, not consume it.

The project should be fun. You will enjoy yourself if you balance project work with other activities. This means taking actual time off to do the other things you enjoy outside work.

Keep aiming for this balance, and *you will* be more productive, work more effectively and creatively. The personal growth you experience from doing research, the things you will learn, will be massive.

So give yourself the best chance to enjoy the journey. Over to Carl for a reminder on why we do this.

.. epigraph::

    "...understanding is an exquisite form of ecstasy..."

    -- Carl Sagan
    

.. rubric:: Footnotes

.. [#] If you aren't prepared to accept that, you should probably do something else.
.. [#] Properties that are problematic now may not have been evident before; hence "the problem" is new.
.. [#] Bearing in mind you must avoid restating it to a question to which you already know the answer from examining your data -- avoid *a posteori* questions.
.. [#] In science, we frame the value of work as its "significance".
.. [#] For challenging algorithmic problems, substitute a competitor in place for where *your* work will fit.
.. [#] In a well designed and executed project, a "failure" will be useful since it reveals some fundamental property that was previously not appreciated. Getting value from a failure requires you to be able to :ref:`avoid uninteresting answers <correctness>`. You need to ensure that failure is not due to an error on your part. If you cannot establish failure as interesting, you likely have a very high-risk project indeed, and you should probably change your project goals.
